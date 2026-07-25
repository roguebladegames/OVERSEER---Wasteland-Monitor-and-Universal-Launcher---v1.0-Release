"""
Fixed read_rtss_fps() for overseer_fps.py

Reconstructed from decompiled bytecode of the shipped OVERSEER.exe
(overseer_fps.pyc) plus two targeted fixes:

  BUG 1 — original code discarded an entry whose instantaneous
  time0/time1/frames delta was momentarily stale *before* ever
  checking whether the process name matched. That meant a correctly
  hooked FalloutNV.exe entry got silently thrown away on any poll
  that landed between RTSS's internal averaging resets.
  FIX: match the process name first; only then try to derive fps.
  If matched but no fps yet, return a distinct "hooked, no sample
  yet" result instead of pretending the entry never existed.

  BUG 2 — the "v2.3+ stat avg" fallback field was read at a fixed
  offset (entry_start + 4 + 260 + 16 + 24) regardless of the
  entry's own declared app_entry_size. On classic/older RTSS
  builds (app_entry_size 272-280, no extended fields) that offset
  lands inside the *next* entry, misreading a neighboring PID/name
  byte as your fps stat.
  FIX: only attempt the stat-avg read if app_entry_size is large
  enough to actually contain that field.

Drop this into overseer_fps.py in place of the existing
read_rtss_fps (and helpers _open_mapping / _map_view / _read_bytes /
_name_matches, included below for completeness -- these were
already correct in the original and are reproduced unchanged).
"""

import ctypes
import logging
import struct

log = logging.getLogger("overseer_fps")

_kernel32 = ctypes.windll.kernel32
FILE_MAP_READ = 0x0004

# CRITICAL: ctypes defaults every function's return type to a 32-bit
# `int` unless told otherwise. MapViewOfFile and OpenFileMappingW both
# return 64-bit pointers/handles on 64-bit Windows -- without these
# declarations the pointer gets silently truncated to 32 bits, which
# is exactly what caused the "access violation" crashes: every
# "address" downstream was garbage.
_kernel32.OpenFileMappingW.restype = ctypes.c_void_p
_kernel32.OpenFileMappingW.argtypes = [ctypes.c_ulong, ctypes.c_int, ctypes.c_wchar_p]

_kernel32.MapViewOfFile.restype = ctypes.c_void_p
_kernel32.MapViewOfFile.argtypes = [
    ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_size_t,
]

_kernel32.UnmapViewOfFile.restype = ctypes.c_int
_kernel32.UnmapViewOfFile.argtypes = [ctypes.c_void_p]

_kernel32.CloseHandle.restype = ctypes.c_int
_kernel32.CloseHandle.argtypes = [ctypes.c_void_p]

_kernel32.VirtualQuery.restype = ctypes.c_size_t
_kernel32.VirtualQuery.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]

# --- unchanged helpers (these were fine in the original) -------------------

def _open_mapping(name):
    h = _kernel32.OpenFileMappingW(FILE_MAP_READ, False, name)
    if not h:
        return None
    return h


class _MEMORY_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_void_p),
        ("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", ctypes.c_ulong),
        ("PartitionId", ctypes.c_ushort),
        ("RegionSize", ctypes.c_size_t),
        ("State", ctypes.c_ulong),
        ("Protect", ctypes.c_ulong),
        ("Type", ctypes.c_ulong),
    ]


def _map_view(handle):
    ptr = _kernel32.MapViewOfFile(handle, FILE_MAP_READ, 0, 0, 0)
    if not ptr:
        return None

    # Query the ACTUAL size of the mapped region -- MapViewOfFile with
    # dwNumberOfBytesToMap=0 maps the whole underlying section, but that
    # section's real size is whatever RTSS allocated (often well under
    # 1 MB), not a fixed constant. Reading past it causes an access
    # violation, which is exactly what happened without this query.
    mbi = _MEMORY_BASIC_INFORMATION()
    result = _kernel32.VirtualQuery(
        ctypes.c_void_p(ptr), ctypes.byref(mbi), ctypes.sizeof(mbi)
    )
    if result == 0:
        _kernel32.UnmapViewOfFile(ptr)
        return None

    region_size = mbi.RegionSize
    if region_size <= 0:
        _kernel32.UnmapViewOfFile(ptr)
        return None

    # NOTE: no artificial cap here -- VirtualQuery already told us the
    # real, safe-to-read size of this mapping. An earlier version of
    # this code capped reads at 2MB (sized for the old ~280-byte-per-app
    # RTSS format) which silently truncated the buffer before reaching
    # the actual app data table on newer RTSS versions with much larger
    # per-app entries (12KB+). Cap only as a sanity ceiling against
    # something absurd, not as a normal-case limit.
    SANITY_CEILING = 64 * 1024 * 1024  # 64MB -- just a guard rail
    return ptr, min(region_size, SANITY_CEILING)


def _read_bytes(ptr, size):
    return ctypes.string_at(ptr, size)


def _name_matches(app_name, targets):
    n = (app_name or "").lower().replace("\\", "/")
    base = n.rsplit("/", 1)[-1]
    bare = {t[:-4] if t.endswith(".exe") else t for t in targets}
    if base in targets or base in bare:
        return True
    if base.replace(".exe", "") in bare:
        return True
    return any(b in n for b in bare)


# --- fixed read_rtss_fps -----------------------------------------------

RTSS_SIGNATURE = 0x52545353  # confirmed against live RTSS 2.21 shared memory dump
                               # (C multi-char constant 'RTSS' packs R as the
                               # most-significant byte -- the original code's
                               # 0x53535452 was byte-order-reversed and never
                               # actually matched real RTSS memory)
MIN_APP_ENTRY_SIZE = 272     # classic RTSS entry: pid + name[260] + 4 dwords
STAT_AVG_MIN_ENTRY_SIZE = 304  # entry must be at least this big to safely
                                # contain the v2.3+ stat-avg dword we read


def read_rtss_fps(process_names, prefer_pid=None):
    """
    Read FPS from RTSS shared memory for a matching game process.
    Supports instantaneous (time0/time1/frames) and v2.3+ stat average.

    Fixed version: name-matches BEFORE deciding whether to discard an
    entry for lacking a fresh fps sample, and bounds-checks the stat-avg
    offset against the entry's own declared size.
    """
    targets = set(process_names) if process_names else {"falloutnv.exe", "falloutnv"}
    targets.update({"falloutnv.exe", "falloutnvng.exe", "nvse_loader.exe", "newvegas.exe"})

    for map_name in ("RTSSSharedMemoryV2", "RTSSSharedMemoryV3"):
        handle = _open_mapping(map_name)
        if not handle:
            continue

        mapped = _map_view(handle)
        if not mapped:
            _kernel32.CloseHandle(handle)
            continue

        ptr, size = mapped
        try:
            raw = _read_bytes(ptr, size)
        finally:
            _kernel32.UnmapViewOfFile(ptr)
            _kernel32.CloseHandle(handle)

        if len(raw) < 32:
            continue

        sig = struct.unpack_from("<I", raw, 0)[0]
        if sig != RTSS_SIGNATURE:
            continue

        version = struct.unpack_from("<I", raw, 4)[0]
        if (version >> 16) < 2:
            continue

        app_entry_size = struct.unpack_from("<I", raw, 8)[0]
        app_arr_offset = struct.unpack_from("<I", raw, 12)[0]
        app_arr_size = struct.unpack_from("<I", raw, 16)[0]

        if app_entry_size < MIN_APP_ENTRY_SIZE or app_arr_size < 1 or app_arr_offset < 32:
            continue
        if app_arr_offset + app_entry_size * app_arr_size > len(raw):
            continue

        best_hooked_but_stale = None  # matched name, but no fps sample yet

        for i in range(int(app_arr_size)):
            off = app_arr_offset + i * app_entry_size
            if off + 16 > len(raw):
                break

            pid = struct.unpack_from("<I", raw, off)[0]
            if pid == 0:
                continue

            name_bytes = raw[off + 4: off + 4 + 260]
            z = name_bytes.find(b"\x00")
            name = (name_bytes[:z] if z >= 0 else name_bytes).decode("mbcs", errors="replace")

            # -------- FIX: name-match FIRST, before we decide fps validity --------
            if prefer_pid is not None:
                hit = (pid == prefer_pid)
            else:
                hit = _name_matches(name, targets)

            if not hit:
                continue  # this entry just isn't our game, safe to skip

            base_off = off + 4 + 260
            if base_off + 16 > len(raw):
                continue

            flags = struct.unpack_from("<I", raw, base_off)[0]
            time0 = struct.unpack_from("<I", raw, base_off + 4)[0]
            time1 = struct.unpack_from("<I", raw, base_off + 8)[0]
            frames = struct.unpack_from("<I", raw, base_off + 12)[0]

            fps = None
            if time1 > time0 and frames > 0:
                inst = frames * 1000.0 / float(time1 - time0)
                if 0.5 < inst <= 1000:
                    fps = inst

            # -------- FIX: only read stat-avg if entry actually contains it --------
            if app_entry_size >= STAT_AVG_MIN_ENTRY_SIZE and base_off + 16 + 24 + 4 <= len(raw):
                try:
                    stat_avg = struct.unpack_from("<I", raw, base_off + 16 + 24)[0]
                except struct.error:
                    stat_avg = None

                if stat_avg is not None:
                    cand = None
                    if 500 <= stat_avg <= 50000:
                        c = stat_avg / 100.0
                        if 1.0 <= c <= 480:
                            cand = c
                    elif 1 <= stat_avg <= 480:
                        cand = float(stat_avg)

                    if cand is not None:
                        fps = cand if fps is None else (0.35 * cand + 0.65 * fps)

            if fps is None:
                # Name matched, pid is real, RTSS has this process --
                # we just don't have a usable sample THIS poll.
                # Remember it so the caller can report "hooked, waiting"
                # instead of the misleading "not running or hooked".
                best_hooked_but_stale = {"pid": pid, "process": name}
                continue

            log.debug("RTSS match: pid=%s name=%r fps=%.2f", pid, name, fps)
            return {
                "ok": True,
                "fps": fps,
                "source": "rtss",
                "process": name,
                "pid": pid,
            }

        if best_hooked_but_stale is not None:
            return {
                "ok": True,
                "fps": None,
                "source": "rtss",
                "process": best_hooked_but_stale["process"],
                "pid": best_hooked_but_stale["pid"],
                "note": "HOOKED — waiting for a fresh RTSS sample (game found, no frame delta yet).",
            }

    return {
        "ok": False,
        "fps": None,
        "source": None,
        "note": "RTSS not running or game not hooked",
    }

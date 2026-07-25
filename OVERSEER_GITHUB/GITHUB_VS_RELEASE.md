# GITHUB vs RELEASE — exact file map

Source inspected: **`OVERSEER-v1.0-Windows.zip`** (PyInstaller onedir, Python 3.11).

---

## Label: GITHUB (this tree)

Commit **only** what you author and what the app needs to run from source.

### Root

| Path | In GitHub? | Notes |
|------|------------|-------|
| `README.md` | **YES** | How to run from source |
| `LICENSE` | **YES** | MIT |
| `requirements.txt` | **YES** | pip deps |
| `.gitignore` | **YES** | |
| `RUN_OVERSEER.bat` | **YES** | Dev launcher |
| `SOURCE_MODULES.md` | **YES** | Module inventory |
| `GITHUB_VS_RELEASE.md` | **YES** | This map |
| `CHANGELOG.md` | **YES** | From dist changelog |
| `klavo.ico` | **YES** | Your icon |
| `overseer_server.py` | **YES** | **Restore from your source** (only `.pyc` in zip) |
| `overseer_paths.py` | **YES** | restore |
| `overseer_core.py` | **YES** | restore |
| `overseer_games.py` | **YES** | restore |
| `overseer_fps.py` | **YES** | restore |
| `overseer_radio.py` | **YES** | restore |
| `overseer.spec` | optional | Packaging recipe (not in release zip; recreate when building) |
| `BUILD_EXE.bat` / `BUILD_DIST.bat` | optional | Mentioned in changelog; not in release zip |

### `web/` — your UI

| Path | In GitHub? |
|------|------------|
| `web/index.html` | **YES** |
| `web/assets/*.png` / `*.jpg` | **YES** (all klavo-* assets) |

### `knowledge/` — your knowledge pack

| Path | In GitHub? |
|------|------------|
| `knowledge/OVERSEER_PROTOCOL.txt` | **YES** |
| `knowledge/FNV_Console_Arsenal.txt` | **YES** |
| `knowledge/FNV_DOWNLOAD_QUEUE.md` | **YES** |
| `knowledge/FNV_Knowledge_Base.md` | **YES** |
| `knowledge/FNV_RAG_Starter_Chunks.json` | **YES** |
| `knowledge/FNV_Source_Links.md` | **YES** |
| `knowledge/_audit_rights_scan.py` | **YES** |
| `knowledge/codex/**` | **YES** (index, originality notice, factions/npcs/quests) |

### `data/` — defaults only

| Path | In GitHub? |
|------|------------|
| `data/config.default.json` | **YES** |
| `data/config.json` | **NO** (user runtime; gitignored) |
| `data/overseer.log` | **NO** (runtime; gitignored) |

### `docs/` / `patches/`

| Path | In GitHub? |
|------|------------|
| `docs/START_HERE.txt`, `docs/README_DIST.txt` | optional (end-user copy from dist) |
| `patches/overseer_fps_rtss_fix.py` | optional (RTSS fix snippet) |

---

## Label: RELEASE ZIP only (Nexus / Windows package)

Ship these to players. **Never** put them in the GitHub source repo.

### Top-level dist

| Path in zip | Keep in release | Keep on GitHub? |
|-------------|-----------------|-----------------|
| `OVERSEER.exe` | YES | **NO** |
| `Launch OVERSEER.bat` | YES | NO (dev uses `RUN_OVERSEER.bat`) |
| `klavo.ico` | YES | YES (source copy) |
| `README.txt` / `START_HERE.txt` / `CHANGELOG.txt` / `LICENSE.txt` | YES | YES as markdown/LICENSE (not required as `.txt` duplicates) |
| `_internal/` entire folder | YES (required next to exe) | **NO** |

### Inside `_internal/` — runtime & third-party (release only)

| Content | Why release-only |
|---------|------------------|
| `python311.dll`, `python3.dll`, `VCRUNTIME140.dll`, `ucrtbase.dll` | Embedded CPython runtime |
| `api-ms-win-*.dll`, `libcrypto-3.dll`, `libssl-3.dll`, `libffi-8.dll` | CRT / OpenSSL / FFI |
| `base_library.zip` | Stdlib archive |
| `*.pyd` (`_socket`, `_ssl`, `unicodedata`, numpy extensions, bcrypt, …) | Frozen C extensions — **not** your source |
| `numpy/`, `numpy.libs/`, `psutil/`, `yaml/`, `markupsafe/`, `bcrypt/`, `cryptography/`, `pythonnet/`, `clr_loader/`, `soundcard/`, `webview/` | Third-party packages + natives |
| `*-dist-info/` folders | Wheel metadata for bundled libs |
| `webview/lib/**` (WebView2 DLLs, runtimes) | pywebview packaging |
| `_portaudiowpatch*.pyd` | Optional audio backend binary |

### Inside `_internal/` — your assets (also on GitHub, different path)

| Path in zip | GitHub equivalent |
|-------------|-------------------|
| `_internal/web/**` | `web/**` |
| `_internal/knowledge/**` | `knowledge/**` |
| `_internal/data/config.default.json` | `data/config.default.json` |
| `_internal/klavo.ico` | `klavo.ico` |

Your Python is **not** under `_internal` as `.py` — it is compiled into `OVERSEER.exe` / `PYZ.pyz` as:

- `overseer_server` (entry)
- `overseer_core`, `overseer_paths`, `overseer_games`, `overseer_fps`, `overseer_radio`

---

## Sane target trees

### GITHUB (source)

```
OVERSEER/
  README.md
  LICENSE
  requirements.txt
  .gitignore
  RUN_OVERSEER.bat
  klavo.ico
  overseer_server.py
  overseer_paths.py
  overseer_core.py
  overseer_games.py
  overseer_fps.py
  overseer_radio.py
  web/
    index.html
    assets/…
  knowledge/
    …
  data/
    config.default.json
```

### RELEASE (player zip)

```
OVERSEER-v1.0/
  OVERSEER.exe
  Launch OVERSEER.bat
  klavo.ico
  README.txt
  START_HERE.txt
  CHANGELOG.txt
  LICENSE.txt
  _internal/          ← entire runtime; do not open-source as “source”
    web/
    knowledge/
    data/config.default.json
    python311.dll
    … DLLs, pyds, third-party trees …
```

---

## Critical rule

| Put on GitHub | Keep only in Nexus zip |
|---------------|------------------------|
| Your `.py`, `web/`, `knowledge/`, defaults, icon, docs, MIT license | `OVERSEER.exe`, `_internal/`, all DLLs, all `.pyd`, embedded Python, vendor folders |

Players need the zip. Contributors need the GitHub tree.

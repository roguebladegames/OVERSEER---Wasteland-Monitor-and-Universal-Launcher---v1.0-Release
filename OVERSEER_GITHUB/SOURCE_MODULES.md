# Python modules expected at the repo root

The **OVERSEER-v1.0 Windows release zip is a PyInstaller package**. Your application logic is frozen inside `OVERSEER.exe` as `.pyc` bytecode — **not** as editable `.py` files and **not** as third-party `.pyd` extensions.

These **six modules** are the app source that belong on GitHub (flat next to `web/`, `knowledge/`, `data/`):

| File | Role (from v1.0 bytecode) |
|------|---------------------------|
| `overseer_server.py` | **Entry point.** Flask app, all `/api/*` routes, optional `pywebview` desktop shell, logging. |
| `overseer_paths.py` | Dev vs frozen paths: `INSTALL_DIR`, `BUNDLE_DIR`, `DATA_DIR`, `WEB_DIR`, `KNOWLEDGE_DIR`, icon + config seed. |
| `overseer_core.py` | Config, knowledge index, mods/plugins scan, Ollama chat, system stats, NVSE/launch helpers, console batch. |
| `overseer_games.py` | Multi-title Fallout catalog, Steam library scan, launchers, process detection. |
| `overseer_fps.py` | Live FPS: RTSS shared memory, MSI Afterburner MAHM, PresentMon capture. |
| `overseer_radio.py` | RobCo Broadcast Relay — WASAPI loopback spectrum (`soundcard` / PyAudioWPatch). |

Also keep (already in this tree):

| File | Role |
|------|------|
| `knowledge/_audit_rights_scan.py` | Utility shipped with the knowledge pack (plain `.py` in the zip). |

## What is *not* in the release as source

- No `overseer_theme.py` in v1.0 (themes live in `web/index.html` CSS/`data-theme`).
- Packaging scripts referenced by the changelog (`overseer.spec`, `BUILD_EXE.bat`, `BUILD_DIST.bat`) were **not** inside the user release zip; recreate them when you package again.

## Where to get the `.py` files

1. **Preferred:** your original project folder / backups / git history before packaging.
2. **Partial:** early prototype zip (`OVERSEER_prototype_v01`) has older `overseer_core.py`, `overseer_server.py`, `overseer_theme.py` — **not** equivalent to v1.0.
3. **Bytecode only (this machine):** extracted under  
   `Downloads\OVERSEER_pyi_extract\OVERSEER.exe_extracted\`  
   (`overseer_server.pyc` + `PYZ.pyz_extracted\overseer_*.pyc`).  
   Full decompile of Python 3.11 bytecode needs a 3.11-capable decompiler (e.g. pycdc).
4. **FPS RTSS fix:** `patches/overseer_fps_rtss_fix.py` is a reconstructed drop-in for `read_rtss_fps` (and helpers), not the whole module.

Until the six root modules are restored, `RUN_OVERSEER.bat` will refuse to start.

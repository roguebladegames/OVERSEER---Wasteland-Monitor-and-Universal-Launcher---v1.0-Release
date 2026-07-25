# OVERSEER

**Unofficial local companion for Fallout installs** — focused on Fallout: New Vegas modding, launch, performance, knowledge search, and optional local LLM chat.

Made by **Klavo** (2026).  
**Not** affiliated with Bethesda, ZeniMax, Microsoft, or Obsidian.

License: [MIT](LICENSE) (plus trademark / fan-work notices in that file).

---

## What it is

OVERSEER is a **local-only** desktop utility:

- Terminal-style UI (RobCo green / Pip-Boy amber) in a WebView2 window (or browser)
- Multi-title Fallout install detection and launch (script extender when present)
- New Vegas plugins / load-order awareness
- Bundled original field-manual knowledge (quests, NPCs, factions, mod notes)
- Optional chat via **local Ollama** (offline snippets if Ollama is down)
- Host CPU/RAM (+ GPU when available)
- Live **in-game FPS** only when a real hook exists (RTSS / Afterburner / PresentMon) — never faked
- **RobCo Broadcast Relay** — system audio loopback visualizer

Default server: `http://127.0.0.1:8765/`

---

## Repository layout (GitHub)

```
OVERSEER/
├── README.md                 # this file
├── LICENSE                   # MIT + fan-work notices
├── requirements.txt
├── RUN_OVERSEER.bat          # run from source on Windows
├── SOURCE_MODULES.md         # which .py files belong here
├── .gitignore
├── CHANGELOG.md
├── klavo.ico                 # app icon
│
├── overseer_server.py        # ENTRY — restore from your source (see SOURCE_MODULES.md)
├── overseer_paths.py
├── overseer_core.py
├── overseer_games.py
├── overseer_fps.py
├── overseer_radio.py
│
├── web/
│   ├── index.html            # full UI (HTML/CSS/JS)
│   └── assets/               # klavo icons / images
│
├── knowledge/                # local knowledge pack
│   ├── OVERSEER_PROTOCOL.txt
│   ├── FNV_*.md / .txt / .json
│   ├── _audit_rights_scan.py
│   └── codex/                # original field notes
│
├── data/
│   └── config.default.json   # shipped defaults (runtime writes config.json here)
│
├── docs/                     # end-user notes from the dist package
└── patches/                  # optional FPS RTSS fix snippet
```

**Do not commit** DLLs, `.pyd` files, `_internal/`, `OVERSEER.exe`, or PyInstaller build trees. Those belong only in the **Nexus / Windows release zip**.

---

## Run from source

### Requirements

- Windows 10/11 64-bit (primary target)
- **Python 3.11+** on PATH
- Microsoft **Edge WebView2** Runtime (usually already on Win11)
- Optional: [Ollama](https://ollama.com) + a chat model (`ollama pull mistral`)
- Optional: RTSS / MSI Afterburner for live FPS

### Steps

1. Restore the six `overseer_*.py` modules to the repo root (see [SOURCE_MODULES.md](SOURCE_MODULES.md)).
2. Double-click `RUN_OVERSEER.bat`, **or**:

```bat
python -m pip install -r requirements.txt
python overseer_server.py
```

3. A WebView2 window should open.  
   Browser fallback:

```bat
set OVERSEER_BROWSER=1
python overseer_server.py
```

Then open `http://127.0.0.1:8765/`.

### Config & logs (runtime)

On first run the app creates writable files under `data/`:

| File | Purpose |
|------|---------|
| `data/config.json` | Paths, theme, Ollama settings (from `config.default.json`) |
| `data/overseer.log` | Troubleshooting |

These are gitignored. Safe to delete `config.json` to reset.

Environment helpers used by the packaged app (also useful in dev):

| Variable | Effect |
|----------|--------|
| `OVERSEER_BROWSER=1` | Open system browser instead of WebView2 |
| `OVERSEER_PORT` | Override HTTP port (default `8765`) |
| `OVERSEER_CONSOLE=1` | Prefer console logging when available |

---

## Release zip vs this repo

| | **GitHub (this repo)** | **Nexus / Windows release zip** |
|--|------------------------|----------------------------------|
| Your `.py` modules | ✅ | ❌ (frozen into `OVERSEER.exe`) |
| `web/`, `knowledge/`, `data/config.default.json`, `klavo.ico` | ✅ | ✅ (under `_internal/`) |
| `README` / `LICENSE` / changelog | ✅ | ✅ (as `.txt`) |
| `OVERSEER.exe` | ❌ | ✅ |
| `_internal/` (Python runtime, DLLs, `.pyd`, numpy, flask wheels, WebView2 natives, …) | ❌ | ✅ |
| Launch batch for end users | optional (`RUN_OVERSEER.bat` for dev) | `Launch OVERSEER.bat` |

See also packaging notes in the dist docs under `docs/`.

---

## Privacy

- Bound to localhost by design
- No OVERSEER cloud account
- LLM traffic only to the Ollama URL you configure (default local)
- No built-in telemetry to the author

---

## Disclaimer

Back up saves and load orders. Console commands and modding can break installs.  
OVERSEER does not ship games, DLC, mods, or official guides.

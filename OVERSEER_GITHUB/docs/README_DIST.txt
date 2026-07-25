OVERSEER v1.0 - Wasteland Monitor
Made by Klavo
=================================

Unofficial, local companion app for Fallout series installs - focused on
Fallout: New Vegas modding, launch, performance, and field notes.

NOT an official Bethesda / ZeniMax / Microsoft product.
See LICENSE.txt for full license, trademark, and fan-work notices.


QUICK START
-----------
  1. Unzip this entire folder somewhere permanent.
     Keep OVERSEER.exe and the _internal\ folder together.
  2. Double-click  OVERSEER.exe
     (or "Launch OVERSEER.bat")
  3. A desktop window opens (Edge WebView2).
  4. Click Detect / scan games, or set paths manually.
  5. Optional: install Ollama and pull a chat model for full AI replies.
  6. Optional: run RTSS or MSI Afterburner for live in-game FPS.


WHAT'S IN THIS FOLDER
---------------------
  START_HERE.txt       One-page first-run guide (read this first)
  README.txt           This file - full user guide
  CHANGELOG.txt        Version history / feature list
  LICENSE.txt          MIT license + fan-work / trademark notices
  Launch OVERSEER.bat  Shortcut launcher
  OVERSEER.exe         Main application (native window)
  klavo.ico            App icon
  _internal\           Runtime libraries, UI, and knowledge pack
                       (required - do not delete)


REQUIREMENTS
------------
  Required
    - Windows 10 or 11 (64-bit)
    - Microsoft Edge WebView2 Runtime
        https://developer.microsoft.com/microsoft-edge/webview2/
      (Usually preinstalled on Windows 11)

  For game launch / load-order tools
    - A legal install of the game(s) you want to use
    - Script extender recommended where applicable
        (e.g. xNVSE for Fallout: New Vegas)

  Optional
    - Ollama for local LLM chat          https://ollama.com
    - RTSS and/or MSI Afterburner for FPS
    - Vortex (or another mod manager) for status detection


FEATURES (v1.0)
---------------
  Desktop shell
    - Native Windows window via WebView2 (not a floating browser tab)
    - RobCo green and Pip-Boy amber themes
    - Local-only server (127.0.0.1) - no cloud account

  Games
    - Multi-title Fallout catalog scan (classic through modern titles
      where present on disk / Steam library folders)
    - Detect install paths, main executables, and common script extenders
    - Launch preferred loader (e.g. NVSE) when available
    - Live "game running" process status

  Mods / load order
    - Scan plugins.txt / load order paths
    - Multi-game mod folder awareness where configured
    - Auto-detect common FNV paths on first boot

  Knowledge + chat
    - Bundled original field-manual knowledge (quests, NPCs, factions,
      modding notes, console cheat-sheet) for local search
    - Chat endpoint with optional local Ollama models
    - Offline fallback: knowledge snippets when Ollama is down
    - Custom system prompt (or reset to default Overseer protocol)
    - Model picker / Ollama URL settings in the UI

  Performance
    - Live host CPU and RAM
    - NVIDIA GPU metrics when drivers/libs allow
    - In-game FPS when a real backend is available:
        RTSS shared memory (preferred), MSI Afterburner (MAHM),
        or PresentMon-style capture if configured
    - Honest "unavailable" state when nothing is hooked
      (OVERSEER does not invent FPS numbers)

  RobCo Broadcast Relay
    - System audio loopback visualizer (WASAPI)
    - Tune-in / stand-by controls
    - Demo carrier if capture libraries fail

  Console helper
    - Write a local console batch for in-game use
      (e.g. bat overseer style workflow - your game, your responsibility)

  Config + logs
    - data\config.json created next to the exe on first run
    - data\overseer.log for troubleshooting


FIRST-RUN CHECKLIST
-------------------
  [ ] WebView2 installed (window opens)
  [ ] Detect finds your game or you set game_path / Data / plugins.txt
  [ ] (Optional) Ollama running + a chat model pulled
  [ ] (Optional) RTSS running if you want live FPS
  [ ] Launch game once from OVERSEER to verify the loader path


PRIVACY
-------
  - Designed for localhost use only
  - No OVERSEER cloud login
  - LLM traffic (if enabled) goes only to the URL you set (default: local Ollama)
  - No built-in telemetry to the author


WHAT OVERSEER IS NOT
--------------------
  - Not a game, DLC, crack, or mod redistributor
  - Not an official strategy guide
  - Not affiliated with Bethesda, ZeniMax, Microsoft, or Obsidian
  - Not a substitute for backing up saves and load orders
  - Does not ship game assets, voice packs, or third-party mods


TROUBLESHOOTING
---------------
  Window does not open
    - Install WebView2 Runtime
    - Or set environment variable OVERSEER_BROWSER=1 to use your browser
      at http://127.0.0.1:8765/

  Chat is weak / offline snippets only
    - Start Ollama and pull a model (example: ollama pull mistral)
    - Check LLM settings URL (default http://127.0.0.1:11434)

  FPS shows unavailable
    - Start RTSS (and the game) so the overlay hooks the process
    - Or MSI Afterburner with shared-memory sensors enabled
    - OVERSEER never fakes FPS

  Radio / Broadcast Relay silent
    - Set your real speakers as the Windows default playback device
    - Stand by, then Tune in again while audio is playing

  Close the OVERSEER window to quit.


CONFIG LOCATION
---------------
  Next to OVERSEER.exe after first run:

    data\config.json
    data\overseer.log

  Safe to delete config.json to reset paths/theme (app recreates defaults).


SOURCE / REBUILD (developers)
-----------------------------
  Source tree (not required for end users):
    BUILD_DIST.bat   - full GUI distribution zip
    BUILD_EXE.bat    - quick PyInstaller build
    RUN_OVERSEER.bat - run from Python without packaging
    requirements.txt


SUPPORT & LIABILITY
-------------------
  Provided AS IS. Back up saves. Use common sense with mods and console
  commands. Full terms: LICENSE.txt

  Made by Klavo - 2026

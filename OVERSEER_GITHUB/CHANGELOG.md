OVERSEER - Changelog
====================
Made by Klavo
Unofficial fan utility. Not affiliated with Bethesda, ZeniMax, or Microsoft.


[1.0.0] - 2026-07-21
--------------------
First public Windows GUI distribution (OVERSEER-v1.0).


Added - desktop application
  - Native Windows shell via Microsoft Edge WebView2 (pywebview)
  - Packaged OVERSEER.exe + _internal runtime (PyInstaller)
  - Launch OVERSEER.bat helper
  - Optional browser fallback (OVERSEER_BROWSER=1 → http://127.0.0.1:8765/)
  - Local-only HTTP service bound to 127.0.0.1
  - Application icon (klavo.ico) and themed UI assets

Added - themes and UI
  - RobCo green theme
  - Pip-Boy amber theme
  - Terminal-style dashboard layout
  - Live status indicators for docs, mods, Ollama, game, Vortex, radio

Added - multi-game catalog
  - Scan common Steam / library roots for Fallout family installs
  - Titles covered when present on disk (catalog-driven):
      Fallout, Fallout 2, Fallout Tactics, Fallout 3, Fallout: New Vegas,
      Fallout 4, Fallout 4 VR, Fallout 76, Fallout Shelter
  - Detect main executables and common script extenders
      (examples: sfall/ddraw, FOSE, xNVSE, F4SE - if the user installed them)
  - Preferred launch path (script extender before vanilla when configured)
  - Selected-game state in config
  - Live process detection for "game running"

Added - New Vegas / modding tools
  - Auto-detect common FNV install + plugins.txt / Data paths
  - Manual path override and save
  - Plugin / load-order scan
  - Multi-game mod scan API for installed titles
  - Vortex process / install status probe (local detection only)
  - Console batch writer for in-game bat workflows
  - NVSE presence check and launch integration

Added - knowledge and chat
  - Bundled original field-manual knowledge pack (local files only)
      * Codex: quests, NPCs, factions (original prose)
      * Modding knowledge base notes
      * Console command / form-ID cheat sheet
      * Overseer system protocol / persona
      * Source links file (pointers only - does not vendor third-party docs)
  - Local document index + search
  - Chat API with optional Ollama backend
  - Offline fallback to knowledge snippets when Ollama is unreachable
  - LLM setup UI: model list, Ollama URL, custom system prompt, reset default
  - No cloud AI account required

Added - performance monitoring
  - Live host CPU % and RAM
  - NVIDIA GPU metrics when pynvml / driver stack is available
  - In-game FPS backends (first usable wins; no invented numbers):
      1) RTSS (RivaTuner Statistics Server) shared memory
      2) MSI Afterburner MAHM shared-memory framerate sensor
      3) PresentMon-style capture path when available/configured
  - FPS status API and capture start/stop endpoints
  - Optional Performance Log Users setup helper (Windows) for PresentMon
  - Honest "unavailable" state when no hook is present

Added - RobCo Broadcast Relay
  - System default-playback loopback capture (WASAPI)
  - Spectrum / waveform visualizer in the UI
  - Tune in / Stand by controls
  - Demo carrier fallback if capture libraries are missing
  - Uses soundcard and/or PyAudioWPatch when installed in the build

Added - packaging and developer tooling
  - overseer.spec PyInstaller recipe (windowed, no console)
  - BUILD_EXE.bat and BUILD_DIST.bat release scripts
  - RUN_OVERSEER.bat for source/dev runs
  - Config defaults shipped as data/config.default.json
  - Runtime config and logs written beside the exe (not inside the zip)

Documentation and legal (this release package)
  - START_HERE.txt - first-run one-pager
  - README.txt - full user guide and feature inventory
  - CHANGELOG.txt - this file
  - LICENSE.txt - MIT + expanded fan-work, trademark, and redistribution notices
  - Explicit statements that OVERSEER does not redistribute game assets,
    official guides, mods, or voice packs


Notes / limitations (honest)
  - Live FPS requires an external hook (RTSS / Afterburner / PresentMon path).
    OVERSEER will not fabricate FPS.
  - Full natural-language chat quality depends on a local Ollama model you install.
  - Knowledge pack is original operational notes, not an official guide.
  - Multi-title support is detect/launch/monitor oriented; deepest mod tools
    remain New Vegas-focused.
  - TTS / character voice packs are not included in v1.0.


[0.1.0] - 2026-07 (prototype)
-----------------------------
Internal prototype (pre-GUI packaging):

  - Flask local server and web UI
  - Knowledge index + Ollama chat
  - FNV path detect, plugins scan, system stats
  - Theme scaffolding
  - Early distribution experiments

Superseded by v1.0 desktop package.


Roadmap ideas (not in this zip)
-------------------------------
  These are NOT promised features - ideas only:

  - Optional text-to-speech for chat replies (generic local TTS)
  - Deeper per-title mod tooling beyond FNV
  - Additional original mechanics codex docs (authored, not wiki dumps)

Any future voice feature will avoid shipping copyrighted game voice assets
or commercial voice-actor clones in the default package.


Copyright
---------
  OVERSEER software: Copyright (c) 2026 Klavo - see LICENSE.txt
  Fallout and related marks: respective owners only
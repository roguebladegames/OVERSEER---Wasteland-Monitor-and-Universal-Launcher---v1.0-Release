@echo off
cd /d "%~dp0"
title OVERSEER (source)
echo.
echo  OVERSEER — run from source
echo  http://127.0.0.1:8765/  (or WebView2 window)
echo.
if not exist "overseer_server.py" (
  echo  ERROR: overseer_server.py is missing.
  echo  Restore the six overseer_*.py modules into this folder.
  echo  See SOURCE_MODULES.md
  pause
  exit /b 1
)
python -m pip install -r requirements.txt -q
if errorlevel 1 (
  echo  Install Python 3.11+ and ensure it is on PATH.
  pause
  exit /b 1
)
set OVERSEER_CONSOLE=1
python overseer_server.py
echo.
pause

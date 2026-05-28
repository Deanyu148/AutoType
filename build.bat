@echo off
echo === AutoType Build ===
echo.

rem Clean previous build
if exist AutoType.exe del AutoType.exe
if exist build rmdir /s /q build
if exist AutoType.spec del AutoType.spec

rem Build single-file exe
pyinstaller ^
    --onefile ^
    --windowed ^
    --name AutoType ^
    --distpath "." ^
    --icon "AutoType.ico" ^
    --add-data "AutoType.ico;." ^
    --hidden-import pynput.keyboard._win32 ^
    --hidden-import pynput.mouse._win32 ^
    --hidden-import pyautogui ^
    --hidden-import pyscreeze ^
    --hidden-import pytweening ^
    --hidden-import yaml ^
    --exclude PyQt5 ^
    --exclude PyQt5-sip ^
    --exclude PyQt6 ^
    --exclude tkinter ^
    --exclude matplotlib ^
    --exclude scipy ^
    --exclude pandas ^
    main.py

rem Clean temp files
if exist build rmdir /s /q build
if exist AutoType.spec del AutoType.spec

if exist AutoType.exe (
    echo.
    echo === Build SUCCESS ===
    for %%A in (AutoType.exe) do echo AutoType.exe  -  %%~zA bytes
) else (
    echo.
    echo === Build FAILED ===
)
pause

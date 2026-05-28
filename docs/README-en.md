# AutoType

A beautiful, cross-platform auto-typing tool. Simulates keyboard input in any application, with both character-by-character realistic typing and instant clipboard paste modes.

## Features

- **Dual Input Modes** — Character-by-character realistic typing (with random delay variance) or instant clipboard paste
- **Special Key Support** — Supports Enter, Tab, Esc, arrow keys, F1–F12 and more via special tokens
- **Preset Management** — Save, load, import/export presets (YAML format), up to 50 presets
- **Global Hotkeys** — F6 to start, F7 to stop, F8 to toggle, works from any window
- **System Tray** — Minimize to tray with quick-access menu
- **10 UI Languages** — 中文, English, 日本語, 한국어, Español, Français, Deutsch, Русский, Português, العربية
- **Always on Top** — Keep the window above others for easy access
- **Countdown Start** — Configurable 0–10 second start delay
- **Adjustable Speed** — 1–200 CPS (characters per second)
- **Line Numbers** — Editor with line numbers and character/word/line counts

## Installation

### Run from Source

```bash
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType
pip install -r requirements.txt
python main.py
```

### Dependencies

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1 — Qt UI framework
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6 — Keyboard simulation + global hotkey listener
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50 — Instant mode
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0 — Preset import/export

### Build EXE (Windows)

```bash
build.bat
```

Or manually:

```bash
pyinstaller --onefile --windowed --name AutoType --icon AutoType.ico --add-data "AutoType.ico;." main.py
```

## Usage

### Basic Operation

1. Type or paste the text you want to auto-type in the left editor panel
2. Adjust typing speed, delay, and mode on the right
3. Click "Start" or press F6 to begin
4. Place your cursor in the target input field during the countdown (3 sec by default)
5. Press F7 to stop at any time

### Special Key Tokens

Use `{KEY}` notation in your text to insert special keys:

| Token | Key |
|---|---|
| `{ENTER}` | Enter |
| `{TAB}` | Tab |
| `{ESC}` | Escape |
| `{SPACE}` | Space |
| `{BACKSPACE}` | Backspace |
| `{DELETE}` | Delete |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | Arrow keys |
| `{HOME}` `{END}` | Home / End |
| `{PAGEUP}` `{PAGEDOWN}` | Page Up / Down |
| `{F1}` … `{F12}` | Function keys |

Example:
```
username{ENTER}password{TAB}{ENTER}Hello World, this is auto-typed text.{ENTER}
```

### Input Modes

- **Realistic** — Sends keystrokes one by one via pynput with random delay variance. Mimics human typing most closely.
- **Instant** — Uses clipboard + Ctrl+V to paste all at once. Fastest option.

### Global Hotkeys

| Key | Action |
|---|---|
| F6 | Start typing |
| F7 | Stop typing |
| F8 | Toggle (start/stop) |

### Preset Management

- Save current text and settings as a preset (up to 50)
- Load presets to restore text and parameters automatically
- Import/export presets as YAML files for sharing and backup
- Filter presets by name, batch delete

## Project Structure

```
AutoType/
├── main.py                     # Entry point
├── build.bat                   # PyInstaller build script
├── AutoType.ico                # Application icon
├── requirements.txt            # Dependencies
├── README.md                   # Chinese README
├── docs/                       # Other language READMEs
│   ├── README-en.md            # English
│   ├── README-ja.md            # 日本語
│   ├── README-ko.md            # 한국어
│   ├── README-es.md            # Español
│   ├── README-fr.md            # Français
│   ├── README-de.md            # Deutsch
│   ├── README-ru.md            # Русский
│   ├── README-pt.md            # Português
│   └── README-ar.md            # العربية
└── src/
    ├── core/
    │   ├── autotyper.py        # Typing engine (threaded)
    │   └── key_simulator.py    # Keyboard simulation (pynput / pyautogui)
    ├── ui/
    │   ├── main_window.py      # Main window
    │   ├── editor_panel.py     # Text editor panel
    │   ├── settings_panel.py   # Settings panel
    │   ├── preset_manager.py   # Preset management
    │   ├── widgets.py          # Custom widgets
    │   └── theme.py            # Theme definitions
    └── utils/
        ├── config.py           # Configuration persistence (JSON)
        └── i18n.py             # Internationalization
```

## Tech Stack

- **GUI**: PySide6 (Qt for Python)
- **Keyboard Simulation**: pynput (realistic mode) / pyautogui (instant mode)
- **Config Storage**: JSON (user settings) / YAML (preset files)
- **Build**: PyInstaller (single-file EXE)

## License

MIT License

## Author

Deanyu148

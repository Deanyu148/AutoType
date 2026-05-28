# AutoType

Ein schönes, plattformübergreifendes Auto-Tipp-Tool. Simuliert Tastatureingaben in beliebigen Anwendungen, mit zeichenweisem realistischem Tippen und sofortigem Einfügen aus der Zwischenablage.

## Funktionen

- **Zwei Eingabemodi** — Zeichenweises realistisches Tippen (mit zufälliger Verzögerungsabweichung) oder sofortiges Einfügen
- **Sondertasten-Unterstützung** — Enter, Tab, Esc, Pfeiltasten, F1–F12 über spezielle Token
- **Voreinstellungen** — Speichern, laden, importieren/exportieren (YAML-Format), bis zu 50
- **Globale Tastenkürzel** — F6 starten, F7 stoppen, F8 umschalten (funktioniert aus jedem Fenster)
- **System-Tray** — In den Infobereich minimieren mit Schnellzugriffsmenü
- **10 UI-Sprachen** — 中文, English, 日本語, 한국어, Español, Français, Deutsch, Русский, Português, العربية
- **Immer im Vordergrund** — Fenster über anderen halten
- **Countdown-Start** — Konfigurierbare Startverzögerung von 0–10 Sekunden
- **Einstellbare Geschwindigkeit** — 1–200 CPS (Zeichen pro Sekunde)
- **Zeilennummern** — Editor mit Zeilennummern und Zeichen-/Wort-/Zeilenzähler

## Installation

### Aus dem Quellcode starten

```bash
git clone https://github.com/Deanyu148/AutoType.git
cd AutoType
pip install -r requirements.txt
python main.py
```

### Abhängigkeiten

- Python 3.9+
- [PySide6](https://pypi.org/project/PySide6/) >= 6.8.2.1 — Qt UI-Framework
- [pynput](https://pypi.org/project/pynput/) >= 1.7.6 — Tastatursimulation + globaler Hotkey-Listener
- [pyautogui](https://pypi.org/project/pyautogui/) >= 0.9.50 — Sofort-Modus
- [PyYAML](https://pypi.org/project/PyYAML/) >= 6.0 — Voreinstellungs-Import/Export

### EXE erstellen (Windows)

```bash
build.bat
```

## Verwendung

### Grundlegende Bedienung

1. Text im linken Editor-Panel eingeben oder einfügen
2. Geschwindigkeit, Verzögerung und Modus rechts einstellen
3. Auf "Start" klicken oder F6 drücken
4. Cursor während des Countdowns (standardmäßig 3 Sek.) im Zielfeld platzieren
5. Jederzeit mit F7 stoppen

### Sondertasten-Token

Verwenden Sie die `{KEY}`-Notation für Sondertasten:

| Token | Taste |
|---|---|
| `{ENTER}` | Eingabe |
| `{TAB}` | Tab |
| `{ESC}` | Escape |
| `{SPACE}` | Leertaste |
| `{BACKSPACE}` | Rücktaste |
| `{DELETE}` | Entfernen |
| `{UP}` `{DOWN}` `{LEFT}` `{RIGHT}` | Pfeiltasten |
| `{HOME}` `{END}` | Pos1 / Ende |
| `{PAGEUP}` `{PAGEDOWN}` | Bild auf / ab |
| `{F1}` … `{F12}` | Funktionstasten |

Beispiel:
```
benutzername{ENTER}passwort{TAB}{ENTER}Hallo Welt, dies ist automatisch getippter Text.{ENTER}
```

### Eingabemodi

- **Realistisch** — Sendet Tastenanschläge einzeln via pynput mit zufälliger Verzögerungsabweichung. Imitiert menschliches Tippen.
- **Sofort** — Verwendet Zwischenablage + Strg+V zum sofortigen Einfügen. Schnellste Option.

### Globale Tastenkürzel

| Taste | Aktion |
|---|---|
| F6 | Eingabe starten |
| F7 | Eingabe stoppen |
| F8 | Umschalten (starten/stoppen) |

## Projektstruktur

```
AutoType/
├── main.py                     # Einstiegspunkt
├── build.bat                   # PyInstaller Build-Skript
├── AutoType.ico                # Anwendungssymbol
├── requirements.txt            # Abhängigkeiten
├── README.md                   # Chinesische README
├── docs/                       # READMEs in anderen Sprachen
└── src/
    ├── core/
    │   ├── autotyper.py        # Eingabe-Engine (Thread)
    │   └── key_simulator.py    # Tastatursimulation
    ├── ui/
    │   ├── main_window.py      # Hauptfenster
    │   ├── editor_panel.py     # Texteditor-Panel
    │   ├── settings_panel.py   # Einstellungs-Panel
    │   ├── preset_manager.py   # Voreinstellungsverwaltung
    │   ├── widgets.py          # Benutzerdefinierte Widgets
    │   └── theme.py            # Theme-Definitionen
    └── utils/
        ├── config.py           # Konfigurationsspeicherung (JSON)
        └── i18n.py             # Internationalisierung
```

## Tech-Stack

- **GUI**: PySide6 (Qt für Python)
- **Tastatursimulation**: pynput / pyautogui
- **Konfigurationsspeicherung**: JSON / YAML
- **Build**: PyInstaller (Einzeldatei-EXE)

## Lizenz

MIT License

## Autor

Deanyu148

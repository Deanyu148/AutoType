from __future__ import annotations

import re
import time
from abc import ABC, abstractmethod

from PySide6.QtWidgets import QApplication


class KeySimulator(ABC):
    @abstractmethod
    def type_char(self, char: str) -> None: ...

    @abstractmethod
    def type_special(self, key_name: str) -> None: ...

    @abstractmethod
    def paste_text(self, text: str) -> None: ...


class RealisticSimulator(KeySimulator):
    def __init__(self, variance_percent: float = 15.0):
        self._variance = variance_percent / 100.0

        try:
            from pynput.keyboard import Controller, Key

            self._controller = Controller()
            self._Key = Key
            self._available = True
        except (ImportError, OSError):
            self._controller = None
            self._Key = None
            self._available = False

    def _check_available(self):
        if not self._available:
            raise RuntimeError("pynput is unavailable on this system.")

    def type_char(self, char: str) -> None:
        self._check_available()
        self._controller.type(char)

    def type_special(self, key_name: str) -> None:
        self._check_available()
        key_map = {
            "ENTER": self._Key.enter,
            "TAB": self._Key.tab,
            "ESC": self._Key.esc,
            "SPACE": self._Key.space,
            "BACKSPACE": self._Key.backspace,
            "UP": self._Key.up,
            "DOWN": self._Key.down,
            "LEFT": self._Key.left,
            "RIGHT": self._Key.right,
            "HOME": self._Key.home,
            "END": self._Key.end,
            "PAGEUP": self._Key.page_up,
            "PAGEDOWN": self._Key.page_down,
            "DELETE": self._Key.delete,
            "F1": self._Key.f1,
            "F2": self._Key.f2,
            "F3": self._Key.f3,
            "F4": self._Key.f4,
            "F5": self._Key.f5,
            "F6": self._Key.f6,
            "F7": self._Key.f7,
            "F8": self._Key.f8,
            "F9": self._Key.f9,
            "F10": self._Key.f10,
            "F11": self._Key.f11,
            "F12": self._Key.f12,
        }
        key = key_map.get(key_name.upper())
        if key:
            self._controller.tap(key)

    def paste_text(self, text: str) -> None:
        for char in text:
            self.type_char(char)


class InstantSimulator(KeySimulator):
    def __init__(self):
        self._clipboard = QApplication.clipboard()

    def type_char(self, char: str) -> None:
        self.paste_text(char)

    def type_special(self, key_name: str) -> None:
        import pyautogui

        key_map = {
            "ENTER": "enter",
            "TAB": "tab",
            "ESC": "esc",
            "SPACE": "space",
            "BACKSPACE": "backspace",
            "UP": "up",
            "DOWN": "down",
            "LEFT": "left",
            "RIGHT": "right",
        }
        mapped = key_map.get(key_name.upper(), key_name.lower())
        try:
            pyautogui.press(mapped)
        except Exception:
            pass

    def paste_text(self, text: str) -> None:
        import pyautogui

        old = self._clipboard.text()
        self._clipboard.setText(text)
        time.sleep(0.02)
        try:
            pyautogui.hotkey("ctrl", "v")
        except Exception:
            pass
        time.sleep(0.03)
        if old:
            try:
                self._clipboard.setText(old)
            except Exception:
                pass


def create_simulator(mode: str, variance_percent: float = 15.0) -> KeySimulator:
    if mode == "instant":
        return InstantSimulator()
    return RealisticSimulator(variance_percent=variance_percent)


_TOKEN_RE = re.compile(r"\{(ENTER|TAB|ESC|SPACE|BACKSPACE|UP|DOWN|LEFT|RIGHT|"
                       r"HOME|END|PAGEUP|PAGEDOWN|DELETE|"
                       r"F1|F2|F3|F4|F5|F6|F7|F8|F9|F10|F11|F12)\}",
                       re.IGNORECASE)


def tokenize_text(text: str) -> list[tuple[str, str]]:
    tokens = []
    pos = 0
    for match in _TOKEN_RE.finditer(text):
        if match.start() > pos:
            chunk = text[pos:match.start()]
            tokens.extend(("char", c) for c in chunk)
        tokens.append(("special", match.group(1).upper()))
        pos = match.end()
    if pos < len(text):
        tokens.extend(("char", c) for c in text[pos:])
    return tokens

from __future__ import annotations

import random
import threading
from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import QObject, Signal, Slot, QThread

from src.core.key_simulator import (
    KeySimulator,
    create_simulator,
    tokenize_text,
)


@dataclass
class TypingConfig:
    text: str
    speed_cps: int = 50
    start_delay: int = 3
    mode: str = "realistic"
    variance_percent: float = 15.0
    loop_enabled: bool = False
    loop_interval: int = 2


class AutoTyper(QObject):
    status_changed = Signal(str)
    countdown_tick = Signal(int)
    progress_updated = Signal(int, int)
    typing_complete = Signal()
    error_occurred = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._config: Optional[TypingConfig] = None
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()
        self._simulator: Optional[KeySimulator] = None
        self._is_running = False

    def prepare(self, config: TypingConfig) -> None:
        self._config = config

    @Slot()
    def execute(self) -> None:
        if self._is_running or self._config is None:
            return

        self._stop_event.clear()
        self._pause_event.clear()
        self._is_running = True

        try:
            self._simulator = create_simulator(
                self._config.mode, self._config.variance_percent
            )
        except Exception as e:
            self.error_occurred.emit(f"sim_create:{e}")
            self._finish()
            return

        try:
            self._run()
        except Exception as e:
            self.error_occurred.emit(f"type:{e}")
        finally:
            self._finish()

    @Slot()
    def stop(self) -> None:
        self._stop_event.set()
        self._pause_event.clear()
        self._is_running = False

    @Slot()
    def pause(self) -> None:
        self._pause_event.set()

    @Slot()
    def resume(self) -> None:
        self._pause_event.clear()

    def _run(self) -> None:
        if not self._run_countdown():
            return

        self.status_changed.emit("typing")
        while not self._stop_event.is_set():
            self._execute_typing_pass()
            if not self._config.loop_enabled or self._stop_event.is_set():
                break
            self._wait_loop_interval()

        if not self._stop_event.is_set():
            self.status_changed.emit("complete")
            self.typing_complete.emit()

    def _run_countdown(self) -> bool:
        delay = self._config.start_delay
        if delay <= 0:
            return True

        self.status_changed.emit("countdown")
        for remaining in range(delay, 0, -1):
            if self._stop_event.is_set():
                return False
            self.countdown_tick.emit(remaining)
            QThread.sleep(1)
        return True

    def _execute_typing_pass(self) -> None:
        tokens = tokenize_text(self._config.text)
        total = len(tokens)
        if total == 0:
            return

        base_delay = 1.0 / max(self._config.speed_cps, 1)

        for i, (token_type, value) in enumerate(tokens):
            if self._stop_event.is_set():
                return

            self._wait_while_paused()
            if self._stop_event.is_set():
                return

            try:
                if token_type == "char":
                    self._simulator.type_char(value)
                elif token_type == "special":
                    self._simulator.type_special(value)
            except Exception:
                pass

            self.progress_updated.emit(i + 1, total)

            delay = self._calculate_delay(base_delay)
            if delay > 0:
                QThread.msleep(int(delay * 1000))

    def _wait_while_paused(self) -> None:
        while self._pause_event.is_set():
            if self._stop_event.is_set():
                return
            QThread.msleep(50)

    def _wait_loop_interval(self) -> None:
        interval = self._config.loop_interval
        for _ in range(int(interval * 10)):
            if self._stop_event.is_set():
                return
            QThread.msleep(100)

    def _calculate_delay(self, base: float) -> float:
        if self._config.variance_percent <= 0:
            return base
        max_var = max(
            self._config.variance_percent / 100.0 * base, 0.001
        )
        offset = random.uniform(-max_var, max_var)
        return max(0.005, base + offset)

    def _finish(self) -> None:
        self._is_running = False
        self._simulator = None

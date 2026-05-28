import ctypes
from ctypes import wintypes

from PySide6.QtCore import Qt, QMetaObject, QRect, Slot
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QMainWindow,
    QSizePolicy,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QProgressBar,
    QLabel,
    QMenuBar,
    QMenu,
    QStatusBar,
    QSystemTrayIcon,
    QMessageBox,
    QApplication,
    QFileDialog,
    QDialog,
)
from PySide6.QtCore import QThread
import sys
import os

from src.utils.config import Config
from src.utils.i18n import tr, set_language, get_language, LANGUAGES
from src.core.autotyper import AutoTyper, TypingConfig
from src.ui.theme import apply_theme
from src.ui.widgets import CardFrame, SectionTitle, StatusIndicator, HotkeyLabel
from src.ui.editor_panel import EditorPanel
from src.ui.settings_panel import SettingsPanel
from src.ui.preset_manager import PresetPanel, PresetManagerDialog, NewPresetDialog, MAX_PRESETS


class MainWindow(QMainWindow):
    def __init__(self, config: Config):
        super().__init__()
        self._config = config
        self._is_typing = False
        self._typing_paused = False
        self._hotkey_listener = None

        # Worker thread
        self._autotyper = AutoTyper()
        self._typing_thread = QThread()
        self._autotyper.moveToThread(self._typing_thread)

        self._setup_ui()
        self._setup_menus()
        self._setup_tray()
        self._connect_signals()
        self._setup_hotkeys()
        self._restore_state()

        self._typing_thread.start()

        self._update_button_states()
        self._refresh_all_ui()

    # ── UI Setup ────────────────────────────────────────────────

    def _setup_ui(self):
        self.setWindowTitle("自动输入")
        self.setMinimumSize(980, 720)
        self.resize(980, 720)

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(14, 14, 14, 14)
        main_layout.setSpacing(14)

        # ── Left panel: Editor + Control bar ──────────────────
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(8)

        self._editor = EditorPanel()
        self._editor.text_changed.connect(self._update_button_states)
        left_layout.addWidget(self._editor, 1)

        # Progress bar
        self._progress = QProgressBar()
        self._progress.setFixedHeight(14)
        self._progress.setVisible(False)
        left_layout.addWidget(self._progress)

        # Control bar: status (left) + buttons (right)
        ctrl_bar = QWidget()
        ctrl_layout = QHBoxLayout(ctrl_bar)
        ctrl_layout.setContentsMargins(4, 2, 0, 2)
        ctrl_layout.setSpacing(6)

        self._status_indicator = StatusIndicator(show_label=True)
        ctrl_layout.addWidget(self._status_indicator)

        self._progress_label = QLabel("")
        self._progress_label.setStyleSheet("color: #6c7086; font-size: 11px;")
        self._progress_label.setVisible(False)
        ctrl_layout.addWidget(self._progress_label)

        ctrl_layout.addStretch()

        # Hotkey hints (compact)
        self._hint_labels = []
        hints = [
            ("F6", tr("hint.start")),
            ("F7", tr("hint.stop")),
            ("F8", tr("hint.toggle")),
        ]
        for key, label in hints:
            ctrl_layout.addWidget(HotkeyLabel(key))
            lbl = QLabel(label)
            lbl.setStyleSheet("color: #6c7086; font-size: 10px;")
            ctrl_layout.addWidget(lbl)
            self._hint_labels.append(lbl)

        ctrl_layout.addSpacing(6)

        self._start_btn = QPushButton("开始")
        self._start_btn.setObjectName("primaryBtn")
        self._start_btn.setMinimumWidth(100)
        self._start_btn.clicked.connect(self._on_start)

        self._pause_btn = QPushButton("暂停")
        self._pause_btn.setEnabled(False)
        self._pause_btn.setMinimumWidth(80)

        self._pause_btn.clicked.connect(self._on_pause)

        self._stop_btn = QPushButton("停止")
        self._stop_btn.setObjectName("stopBtn")
        self._stop_btn.setEnabled(False)
        self._stop_btn.setMinimumWidth(80)
        self._stop_btn.clicked.connect(self._on_stop)

        ctrl_layout.addWidget(self._start_btn)
        ctrl_layout.addWidget(self._pause_btn)
        ctrl_layout.addWidget(self._stop_btn)

        left_layout.addWidget(ctrl_bar)

        main_layout.addWidget(left_panel, 1)

        # ── Right panel: Settings + Presets ───────────────────
        right_widget = QWidget()
        right_widget.setMinimumWidth(360)
        right_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(8)

        self._settings = SettingsPanel(self._config)
        self._settings._always_on_top_cb.toggled.connect(self._on_always_on_top)
        self._settings.language_changed.connect(self._switch_language)
        right_layout.addWidget(self._settings)

        self._presets = PresetPanel(self._config)
        self._presets.preset_loaded.connect(self._on_preset_loaded)
        self._presets.preset_saved.connect(self._on_preset_saved)
        right_layout.addWidget(self._presets, 1)

        main_layout.addWidget(right_widget, 1)

        # ── Status Bar ──────────────────────────────────────
        self._setup_status_bar()

    def _setup_status_bar(self):
        self._statusbar = QStatusBar()
        self.setStatusBar(self._statusbar)

        self._sb_status = QLabel(tr("state.ready"))
        self._statusbar.addWidget(self._sb_status)

        self._sb_preset = QLabel("")
        self._statusbar.addPermanentWidget(self._sb_preset)

    def _setup_menus(self):
        menubar = self.menuBar()

        # File menu
        self._file_menu = menubar.addMenu(tr("menu.file"))

        self._new_action = QAction(tr("menu.new_preset"), self)
        self._new_action.setShortcut(QKeySequence("Ctrl+N"))
        self._new_action.triggered.connect(self._on_new_preset)
        self._file_menu.addAction(self._new_action)

        self._file_menu.addSeparator()

        self._import_action = QAction(tr("menu.import"), self)
        self._import_action.setShortcut(QKeySequence("Ctrl+I"))
        self._import_action.triggered.connect(self._on_import_file)
        self._file_menu.addAction(self._import_action)

        self._export_action = QAction(tr("menu.export"), self)
        self._export_action.setShortcut(QKeySequence("Ctrl+E"))
        self._export_action.triggered.connect(self._on_export_file)
        self._file_menu.addAction(self._export_action)

        self._file_menu.addSeparator()

        self._exit_action = QAction(tr("menu.exit"), self)
        self._exit_action.setShortcut(QKeySequence("Alt+F4"))
        self._exit_action.triggered.connect(self.close)
        self._file_menu.addAction(self._exit_action)

        # Language menu (dynamic)
        self._lang_menu = menubar.addMenu(tr("menu.language"))
        self._lang_actions: dict[str, QAction] = {}
        for code, name in LANGUAGES.items():
            action = QAction(name, self)
            action.setCheckable(True)
            action.triggered.connect(lambda checked, c=code: self._switch_language(c))
            self._lang_menu.addAction(action)
            self._lang_actions[code] = action
        self._update_lang_check()

        # Window menu
        self._window_menu = menubar.addMenu(tr("menu.window"))

        self._aot_action = QAction(tr("menu.always_on_top"), self)
        self._aot_action.setCheckable(True)
        self._aot_action.setShortcut(QKeySequence("Alt+T"))
        self._aot_action.setChecked(self._config.always_on_top)
        self._aot_action.toggled.connect(self._on_always_on_top)
        self._window_menu.addAction(self._aot_action)

        # Help menu
        self._help_menu = menubar.addMenu(tr("menu.help"))

        self._hotkeys_action = QAction(tr("menu.hotkey_ref"), self)
        self._hotkeys_action.setShortcut(QKeySequence("F1"))
        self._hotkeys_action.triggered.connect(self._show_hotkey_reference)
        self._help_menu.addAction(self._hotkeys_action)

        self._help_menu.addSeparator()

        self._about_action = QAction(tr("menu.about"), self)
        self._about_action.triggered.connect(self._show_about)
        self._help_menu.addAction(self._about_action)

    def _setup_tray(self):
        if not QSystemTrayIcon.isSystemTrayAvailable():
            return

        self._tray = QSystemTrayIcon(self)
        self._tray.setIcon(self.windowIcon())
        self._tray.setToolTip(tr("tray.tooltip"))

        self._tray_menu = QMenu()

        self._tray_show_action = self._tray_menu.addAction(tr("tray.show_hide"))
        self._tray_show_action.triggered.connect(self._toggle_visible)

        self._tray_menu.addSeparator()

        self._tray_start_action = self._tray_menu.addAction(tr("tray.start"))
        self._tray_start_action.triggered.connect(self._on_start)

        self._tray_stop_action = self._tray_menu.addAction(tr("tray.stop"))
        self._tray_stop_action.triggered.connect(self._on_stop)

        self._tray_menu.addSeparator()

        self._tray_quit_action = self._tray_menu.addAction(tr("tray.quit"))
        self._tray_quit_action.triggered.connect(self.close)

        self._tray.setContextMenu(self._tray_menu)
        self._tray.activated.connect(self._on_tray_activated)
        self._tray.show()

    # ── Signal Wiring ───────────────────────────────────────────

    def _connect_signals(self):
        self._autotyper.status_changed.connect(self._on_status_changed)
        self._autotyper.countdown_tick.connect(self._on_countdown_tick)
        self._autotyper.progress_updated.connect(self._on_progress)
        self._autotyper.typing_complete.connect(self._on_typing_done)
        self._autotyper.error_occurred.connect(self._on_typing_error)

    # ── Hotkey Setup ────────────────────────────────────────────

    def _setup_hotkeys(self):
        try:
            from pynput import keyboard

            def on_press(key):
                try:
                    if hasattr(key, "name"):
                        kname = key.name
                    elif hasattr(key, "char") and key.char is not None:
                        return
                    else:
                        return

                    if kname == "f6":
                        QMetaObject.invokeMethod(
                            self, "_on_hotkey_start", Qt.QueuedConnection
                        )
                    elif kname == "f7":
                        QMetaObject.invokeMethod(
                            self, "_on_hotkey_stop", Qt.QueuedConnection
                        )
                    elif kname == "f8":
                        QMetaObject.invokeMethod(
                            self, "_on_hotkey_toggle", Qt.QueuedConnection
                        )
                except Exception:
                    pass

            self._hotkey_listener = keyboard.Listener(on_press=on_press)
            self._hotkey_listener.daemon = True
            self._hotkey_listener.start()
        except (ImportError, OSError):
            pass

    # ── Hotkey Slots ────────────────────────────────────────────

    @Slot()
    def _on_hotkey_start(self):
        if not self._is_typing:
            self._on_start()

    @Slot()
    def _on_hotkey_stop(self):
        if self._is_typing:
            self._on_stop()

    @Slot()
    def _on_hotkey_toggle(self):
        if self._is_typing:
            self._on_stop()
        else:
            self._on_start()

    # ── Actions ─────────────────────────────────────────────────

    def _on_start(self):
        if self._is_typing:
            return

        text = self._editor.get_text()
        if not text.strip():
            QMessageBox.warning(self, tr("dlg.no_text"), tr("dlg.enter_text"))
            return

        # Build config
        config = TypingConfig(
            text=text,
            speed_cps=self._settings.get_speed_cps(),
            start_delay=self._settings.get_start_delay(),
            mode=self._settings.get_mode(),
            variance_percent=self._settings.get_variance(),
        )

        self._is_typing = True
        self._typing_paused = False

        self._progress.setMaximum(len(text))
        self._progress.setValue(0)
        self._progress.setVisible(True)
        self._progress_label.setText(f"(0/{len(text)})")
        self._progress_label.setVisible(True)

        self._update_button_states()
        self._settings.save_to_config()

        self._autotyper.prepare(config)
        QMetaObject.invokeMethod(
            self._autotyper,
            "execute",
            Qt.QueuedConnection,
        )

    def _on_stop(self):
        if not self._is_typing:
            return
        self._autotyper.stop()
        self._reset_ui_state()

    def _on_pause(self):
        if not self._is_typing:
            return
        if self._typing_paused:
            self._autotyper.resume()
            self._typing_paused = False
            self._pause_btn.setText(tr("btn.pause"))
            self._start_btn.setText(tr("state.running"))
        else:
            self._autotyper.pause()
            self._typing_paused = True
            self._pause_btn.setText(tr("btn.resume"))
            self._start_btn.setText(tr("state.paused"))

    # ── Signal Handlers ─────────────────────────────────────────

    @Slot(str)
    def _on_status_changed(self, status: str):
        self._status_indicator.set_status(status)
        self._sb_status.setText(tr(f"state.{status}"))
        if status == "typing":
            self._start_btn.setText(tr("state.running"))
        elif status == "countdown":
            pass  # countdown_tick handles the button text

    @Slot(int)
    def _on_countdown_tick(self, remaining: int):
        self._start_btn.setText(f"{remaining}...")

    @Slot(int, int)
    def _on_progress(self, current: int, total: int):
        if total != self._progress.maximum():
            self._progress.setMaximum(total)
        self._progress.setValue(current)
        self._progress_label.setText(f"({current}/{total})")

    @Slot()
    def _on_typing_done(self):
        self._reset_ui_state()

    @Slot(str)
    def _on_typing_error(self, error_msg: str):
        self._status_indicator.set_status("error")
        self._sb_status.setText(tr("state.error") + f": {error_msg}")
        self._reset_ui_state()
        QMessageBox.critical(self, tr("dlg.typing_error"), error_msg)

    def _reset_ui_state(self):
        self._is_typing = False
        self._typing_paused = False
        self._start_btn.setText(tr("btn.start"))
        self._pause_btn.setText(tr("btn.pause"))
        self._progress.setVisible(False)
        self._progress.setValue(0)
        self._progress_label.setVisible(False)
        self._status_indicator.set_status("ready")
        self._sb_status.setText(tr("state.ready"))
        self._update_button_states()

    def _update_button_states(self):
        has_text = not self._editor.is_empty()
        if self._is_typing:
            self._start_btn.setEnabled(False)
            self._pause_btn.setEnabled(True)
            self._stop_btn.setEnabled(True)
        else:
            self._start_btn.setEnabled(has_text)
            self._pause_btn.setEnabled(False)
            self._stop_btn.setEnabled(False)

    # ── Preset Handling ─────────────────────────────────────────

    def _on_preset_loaded(self, text: str):
        self._editor.set_text(text)
        self._sb_preset.setText(
            f"{tr('status.preset')}: {self._presets.get_current_preset_name()}"
        )
        preset_id = self._presets.get_selected_preset_id()
        if preset_id:
            preset = self._config.get_preset(preset_id)
            if preset and preset.get("params"):
                self._settings.apply_params(preset["params"])

    def _on_preset_saved(self, text: str):
        current_text = self._editor.get_text()
        params = {
            "speed_cps": self._settings.get_speed_cps(),
            "start_delay": self._settings.get_start_delay(),
            "mode": self._settings.get_mode(),
            "variance_percent": self._settings.get_variance(),
        }
        self._presets.request_save_with_text(current_text, params)

    def _on_new_preset(self):
        if len(self._config.list_presets()) >= MAX_PRESETS:
            QMessageBox.warning(
                self, tr("dlg.limit_reached"),
                tr("dlg.limit_msg").format(MAX_PRESETS)
            )
            return

        current_settings = {
            "speed_cps": self._settings.get_speed_cps(),
            "start_delay": self._settings.get_start_delay(),
            "mode": self._settings.get_mode(),
            "variance_percent": self._settings.get_variance(),
        }
        dialog = NewPresetDialog(
            self._config,
            self._editor.get_text(),
            current_settings,
            self,
        )
        if dialog.exec() == QDialog.Accepted:
            self._presets._refresh_list()

    # ── File Operations ─────────────────────────────────────────

    def _on_import_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "导入文本文件",
            "",
            "文本文件 (*.txt *.md *.py *.json *.html *.css *.js);;所有文件 (*)",
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self._editor.set_text(f.read())
            except (OSError, UnicodeDecodeError) as e:
                QMessageBox.critical(
                    self, "导入错误", f"读取文件失败:\n{e}"
                )

    def _on_export_file(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "导出到文件",
            "",
            "文本文件 (*.txt);;所有文件 (*)",
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(self._editor.get_text())
            except OSError as e:
                QMessageBox.critical(
                    self, "导出错误", f"写入文件失败:\n{e}"
                )

    # ── Language ────────────────────────────────────────────────

    def _switch_language(self, lang: str):
        if get_language() == lang:
            return
        set_language(lang)
        self._config._data["language"] = lang
        self._config.save()
        self._refresh_all_ui()

    def _update_lang_check(self):
        cur = get_language()
        for code, action in self._lang_actions.items():
            action.setChecked(code == cur)

    def retranslate_ui(self):
        self.setWindowTitle(tr("app.title"))
        # Menu bar
        self._file_menu.setTitle(tr("menu.file"))
        self._new_action.setText(tr("menu.new_preset"))
        self._import_action.setText(tr("menu.import"))
        self._export_action.setText(tr("menu.export"))
        self._exit_action.setText(tr("menu.exit"))
        self._lang_menu.setTitle(tr("menu.language"))
        for code, action in self._lang_actions.items():
            action.setText(LANGUAGES[code])
        self._window_menu.setTitle(tr("menu.window"))
        self._aot_action.setText(tr("menu.always_on_top"))
        self._help_menu.setTitle(tr("menu.help"))
        self._hotkeys_action.setText(tr("menu.hotkey_ref"))
        self._about_action.setText(tr("menu.about"))
        # Buttons (keep state-aware text)
        if not self._is_typing:
            self._start_btn.setText(tr("btn.start"))
        key = "btn.resume" if self._typing_paused else "btn.pause"
        self._pause_btn.setText(tr(key))
        self._stop_btn.setText(tr("btn.stop"))
        # Hotkey hints
        hints = [tr("hint.start"), tr("hint.stop"), tr("hint.toggle")]
        for i, lbl in enumerate(self._hint_labels):
            if i < len(hints):
                lbl.setText(hints[i])
        self._progress_label.setText("")
        # Status bar
        if not self._is_typing:
            self._sb_status.setText(tr("state.ready"))
        self._sb_preset.setText(
            f"{tr('status.preset')}: {self._presets.get_current_preset_name()}"
        )
        # Tray
        if hasattr(self, "_tray"):
            self._tray.setToolTip(tr("tray.tooltip"))
            self._tray_show_action.setText(tr("tray.show_hide"))
            self._tray_start_action.setText(tr("tray.start"))
            self._tray_stop_action.setText(tr("tray.stop"))
            self._tray_quit_action.setText(tr("tray.quit"))

    # ── View Toggles ────────────────────────────────────────────

    def _on_always_on_top(self, checked: bool):
        self._config.always_on_top = checked
        self._config.save()
        self._apply_topmost(checked)
        self._aot_action.blockSignals(True)
        self._aot_action.setChecked(checked)
        self._aot_action.blockSignals(False)
        self._settings._always_on_top_cb.blockSignals(True)
        self._settings._always_on_top_cb.setChecked(checked)
        self._settings._always_on_top_cb.blockSignals(False)

    def _apply_topmost(self, enabled: bool):
        HWND_TOPMOST = -1
        HWND_NOTOPMOST = -2
        SWP_NOMOVE = 0x0002
        SWP_NOSIZE = 0x0001
        SWP_NOACTIVATE = 0x0010
        flag = HWND_TOPMOST if enabled else HWND_NOTOPMOST
        ctypes.windll.user32.SetWindowPos(
            wintypes.HWND(int(self.winId())),
            wintypes.HWND(flag),
            0, 0, 0, 0,
            SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE,
        )


    def _toggle_visible(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()

    def _on_tray_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self._toggle_visible()

    # ── Dialogs ─────────────────────────────────────────────────

    def _show_hotkey_reference(self):
        QMessageBox.information(self, tr("hotkey.title"), tr("hotkey.text"))

    def _show_about(self):
        QMessageBox.about(self, tr("about.title"), tr("about.text"))

    # ── State Management ────────────────────────────────────────

    def _refresh_all_ui(self):
        """Re-sync all widget texts and status bar after init or language change."""
        self._editor.retranslate_ui()
        self._settings.retranslate_ui()
        self._presets.retranslate_ui()
        self.retranslate_ui()
        self._update_lang_check()
        self._update_button_states()
        current = self.size()
        hint = self.minimumSizeHint()
        if current.width() < hint.width() or current.height() < hint.height():
            self.resize(max(current.width(), hint.width()), max(current.height(), hint.height()))

    def _restore_state(self):
        if self._config.window_maximized:
            self.showMaximized()
        else:
            self.setGeometry(
                self._config.window_x,
                self._config.window_y,
                self._config.window_width,
                self._config.window_height,
            )

        if self._config.always_on_top:
            self._apply_topmost(True)

    def _save_state(self):
        if self.isMaximized():
            self._config.window_maximized = True
        else:
            self._config.window_maximized = False
            geo = self.geometry()
            self._config.window_x = geo.x()
            self._config.window_y = geo.y()
            self._config.window_width = geo.width()
            self._config.window_height = geo.height()
        self._settings.save_to_config()
        self._config.save()

    # ── Clean Shutdown ──────────────────────────────────────────

    def closeEvent(self, event):
        if self._is_typing:
            reply = QMessageBox.question(
                self,
                tr("dlg.typing_in_progress"),
                tr("dlg.stop_and_exit"),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if reply == QMessageBox.No:
                event.ignore()
                return
            self._autotyper.stop()

        self._save_state()

        if self._hotkey_listener and self._hotkey_listener.is_alive():
            self._hotkey_listener.stop()

        self._typing_thread.quit()
        if not self._typing_thread.wait(3000):
            self._typing_thread.terminate()
            self._typing_thread.wait()

        event.accept()

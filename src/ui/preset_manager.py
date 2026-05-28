from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QSizePolicy,
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QVBoxLayout,
    QHBoxLayout,
    QDialog,
    QListWidget,
    QPlainTextEdit,
    QLineEdit,
    QMessageBox,
    QInputDialog,
    QFileDialog,
    QSpinBox,
    QRadioButton,
    QButtonGroup,
    QGroupBox,
    QCheckBox,
    QDialogButtonBox,
    QFormLayout,
    QScrollArea,
)

from src.ui.theme import TEXT_SECONDARY
from src.ui.widgets import SectionTitle, CardFrame
from src.utils.config import Config
from src.utils.i18n import tr


class PresetPanel(CardFrame):
    preset_loaded = Signal(str)
    preset_saved = Signal(str)

    def __init__(self, config: Config, parent=None):
        super().__init__(parent)
        self._config = config
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setMinimumHeight(135)
        self.card_layout.setContentsMargins(10, 4, 10, 8)
        self.card_layout.setSpacing(3)

        self._preset_title = SectionTitle(tr("section.presets"))
        self.addWidget(self._preset_title)

        self._combo = QComboBox()
        self._combo.setMinimumWidth(160)
        self._combo.setFixedHeight(32)
        self.addWidget(self._combo)

        btn_row = QHBoxLayout()
        btn_row.setContentsMargins(0, 0, 0, 0)
        btn_row.setSpacing(4)

        self._load_btn = QPushButton("加载")
        self._load_btn.clicked.connect(self._on_load)
        self._load_btn.setFixedHeight(30)
        self._load_btn.setMinimumWidth(60)
        self._save_btn = QPushButton("保存")
        self._save_btn.clicked.connect(self._on_save)
        self._save_btn.setFixedHeight(30)
        self._save_btn.setMinimumWidth(60)
        self._delete_btn = QPushButton("删除")
        self._delete_btn.clicked.connect(self._on_delete)
        self._delete_btn.setObjectName("dangerBtn")
        self._delete_btn.setFixedHeight(30)
        self._delete_btn.setMinimumWidth(70)

        btn_row.addWidget(self._load_btn)
        btn_row.addWidget(self._save_btn)
        btn_row.addWidget(self._delete_btn)
        self.addLayout(btn_row)

        self._manage_btn = QPushButton(tr("btn.manage_presets"))
        self._manage_btn.setObjectName("secondaryBtn")
        self._manage_btn.setFixedHeight(30)
        self._manage_btn.setMinimumWidth(180)
        self._manage_btn.clicked.connect(self._on_manage)
        self.addWidget(self._manage_btn)

        self._count_label = QLabel()
        self._count_label.setStyleSheet(
            f"color: {TEXT_SECONDARY}; font-size: 10px; padding-top: 2px;"
        )
        self.addWidget(self._count_label)

        self._refresh_list()

    def _refresh_list(self):
        current = self._combo.currentData()
        self._combo.blockSignals(True)
        self._combo.clear()
        presets = self._config.list_presets()
        if not presets:
            self._combo.addItem(tr("presets.no_presets"), None)
        else:
            selected_idx = 0
            for i, p in enumerate(presets):
                self._combo.addItem(p["name"], p["id"])
                if p["id"] == current:
                    selected_idx = i
            self._combo.setCurrentIndex(selected_idx)
        self._combo.blockSignals(False)
        self._count_label.setText(
            tr("presets.count").format(len(self._config.list_presets()), MAX_PRESETS)
        )
        self._update_button_states()

    def _update_button_states(self):
        has_selection = self._combo.currentData() is not None
        self._load_btn.setEnabled(has_selection)
        self._delete_btn.setEnabled(has_selection)

    def _on_load(self):
        preset_id = self._combo.currentData()
        if preset_id:
            preset = self._config.get_preset(preset_id)
            if preset:
                self.preset_loaded.emit(preset["text"])

    def _on_save(self):
        text = ""
        self.preset_saved.emit(text)

    def request_save_with_text(self, text: str, params: dict | None = None):
        if len(self._config.list_presets()) >= MAX_PRESETS:
            QMessageBox.warning(
                self, tr("dlg.limit_reached"), tr("dlg.limit_msg").format(MAX_PRESETS)
            )
            return
        name, ok = QInputDialog.getText(
            self, tr("dlg.save_preset"), tr("dlg.preset_name"), text=""
        )
        if ok and name.strip():
            self._config.add_preset(name.strip(), text, params)
            self._refresh_list()

    def _on_delete(self):
        preset_id = self._combo.currentData()
        if preset_id:
            preset = self._config.get_preset(preset_id)
            name = preset["name"] if preset else "未知"
            reply = QMessageBox.warning(
                self,
                tr("dlg.delete_preset"),
                tr("dlg.delete_confirm").format(name),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                self._config.remove_preset(preset_id)
                self._refresh_list()

    def _on_manage(self):
        dialog = PresetManagerDialog(self._config, self)
        dialog.exec()
        self._refresh_list()

    def retranslate_ui(self):
        self._preset_title.setText(tr("section.presets"))
        self._load_btn.setText(tr("btn.load"))
        self._save_btn.setText(tr("btn.save"))
        self._delete_btn.setText(tr("btn.delete"))
        self._manage_btn.setText(tr("btn.manage_presets"))
        self._refresh_list()

    def get_current_preset_name(self) -> str:
        return self._combo.currentText()

    def get_selected_preset_id(self) -> str | None:
        return self._combo.currentData()


class PresetManagerDialog(QDialog):
    def __init__(self, config: Config, parent=None):
        super().__init__(parent)
        self._config = config
        self.setWindowTitle(tr("section.manage_presets"))
        self.setMinimumSize(700, 480)
        self.resize(750, 500)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        self._dlg_title = SectionTitle(tr("section.manage_presets"))
        layout.addWidget(self._dlg_title)

        search_row = QHBoxLayout()
        self._search = QLineEdit()
        self._search.setPlaceholderText(tr("presets.filter"))
        self._search.textChanged.connect(self._on_filter)
        search_row.addWidget(self._search, 1)

        self._dlg_count_label = QLabel()
        self._dlg_count_label.setStyleSheet(
            f"color: {TEXT_SECONDARY}; font-size: 11px;"
        )
        search_row.addWidget(self._dlg_count_label)
        layout.addLayout(search_row)

        # List + Preview (fixed layout)
        content_row = QHBoxLayout()
        content_row.setSpacing(12)

        left = QWidget()
        left.setFixedWidth(300)
        left_layout = QVBoxLayout(left)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(4)

        left_actions = QHBoxLayout()
        left_actions.setContentsMargins(0, 0, 0, 0)
        rename_btn = QPushButton(tr("btn.rename"))
        rename_btn.clicked.connect(self._on_rename)
        rename_btn.setObjectName("secondaryBtn")
        delete_btn = QPushButton(tr("btn.delete"))
        delete_btn.clicked.connect(self._on_delete_item)
        delete_btn.setObjectName("dangerBtn")
        self._delete_all_btn = QPushButton(tr("btn.delete_all"))
        self._delete_all_btn.clicked.connect(self._on_delete_all)
        self._delete_all_btn.setObjectName("dangerBtn")
        left_actions.addWidget(rename_btn)
        left_actions.addWidget(delete_btn)
        left_actions.addWidget(self._delete_all_btn)
        left_actions.addStretch()
        left_layout.addLayout(left_actions)

        self._list_widget = QListWidget()
        self._list_widget.currentItemChanged.connect(self._on_selection_changed)
        left_layout.addWidget(self._list_widget, 1)

        content_row.addWidget(left)

        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(4)
        right_layout.addWidget(QLabel(tr("presets.preview")))

        self._preview = QPlainTextEdit()
        self._preview.setReadOnly(True)
        right_layout.addWidget(self._preview, 1)

        content_row.addWidget(right, 1)
        layout.addLayout(content_row, 1)

        # Bottom buttons
        buttons = QDialogButtonBox()
        load_btn = buttons.addButton(tr("btn.load"), QDialogButtonBox.AcceptRole)
        load_btn.setObjectName("primaryBtn")
        import_btn = QPushButton(tr("btn.import_presets"))
        import_btn.clicked.connect(self._on_import_presets)
        import_btn.setObjectName("secondaryBtn")
        export_btn = QPushButton(tr("btn.export"))
        export_btn.clicked.connect(self._on_export_dialog)
        export_btn.setObjectName("secondaryBtn")
        close_btn = buttons.addButton(tr("btn.close"), QDialogButtonBox.RejectRole)
        buttons.addButton(import_btn, QDialogButtonBox.ActionRole)
        buttons.addButton(export_btn, QDialogButtonBox.ActionRole)

        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(self._on_load)
        layout.addWidget(buttons)

        self._refresh_list()

    def _refresh_list(self, filter_text: str = ""):
        self._list_widget.clear()
        all_presets = self._config.list_presets()
        self._dlg_count_label.setText(
            tr("presets.count").format(len(all_presets), MAX_PRESETS)
        )
        for p in all_presets:
            if filter_text and filter_text.lower() not in p["name"].lower():
                continue
            self._list_widget.addItem(p["name"])
            self._list_widget.item(
                self._list_widget.count() - 1
            ).setData(Qt.UserRole, p["id"])

    def _on_filter(self, text: str):
        self._refresh_list(text)

    def _on_selection_changed(self, current, previous):
        if current:
            preset_id = current.data(Qt.UserRole)
            preset = self._config.get_preset(preset_id)
            if preset:
                params = preset.get("params", {})
                if params:
                    mode_text = tr("presets.mode_instant") if params.get("mode") == "instant" else tr("presets.mode_char")
                    param_lines = [
                        f"{tr('settings.speed')}: {params.get('speed_cps', '?')} {tr('unit.cps')}",
                        f"{tr('settings.delay')}: {params.get('start_delay', '?')} {tr('unit.sec')}",
                        f"{tr('settings.mode_group')}: {mode_text}",
                        f"{tr('settings.variance')}: {params.get('variance_percent', '?')}{tr('unit.pct')}",
                    ]
                    header = "  |  ".join(param_lines) + "\n" + "─" * 40 + "\n\n"
                else:
                    header = f"({tr('presets.no_params')})\n" + "─" * 40 + "\n\n"
                self._preview.setPlainText(header + preset["text"])
            else:
                self._preview.clear()
        else:
            self._preview.clear()

    def _on_rename(self):
        item = self._list_widget.currentItem()
        if not item:
            return
        preset_id = item.data(Qt.UserRole)
        name, ok = QInputDialog.getText(
            self, tr("dlg.rename_preset"), tr("dlg.new_name"), text=item.text()
        )
        if ok and name.strip():
            self._config.rename_preset(preset_id, name.strip())
            self._refresh_list(self._search.text())

    def _on_delete_item(self):
        item = self._list_widget.currentItem()
        if not item:
            return
        preset_id = item.data(Qt.UserRole)
        reply = QMessageBox.warning(
            self,
            tr("dlg.delete_preset"),
            tr("dlg.delete_confirm").format(item.text()),
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self._config.remove_preset(preset_id)
            self._refresh_list(self._search.text())

    def _on_delete_all(self):
        phrase = tr("dlg.delete_all_phrase")
        dialog = QDialog(self)
        dialog.setWindowTitle(tr("dlg.confirm"))
        dialog.setFixedSize(480, 180)

        dl = QVBoxLayout(dialog)
        dl.setContentsMargins(20, 16, 20, 16)
        dl.setSpacing(12)

        prompt_label = QLabel(tr("dlg.delete_all_prompt"))
        prompt_label.setWordWrap(True)
        prompt_label.setTextInteractionFlags(Qt.NoTextInteraction)
        dl.addWidget(prompt_label)

        input_edit = QLineEdit()
        input_edit.setPlaceholderText(phrase)
        dl.addWidget(input_edit)

        btn_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_box.accepted.connect(dialog.accept)
        btn_box.rejected.connect(dialog.reject)
        dl.addWidget(btn_box)

        if dialog.exec() != QDialog.Accepted:
            return

        if input_edit.text().strip() != phrase:
            QMessageBox.warning(self, tr("dlg.confirm"), tr("dlg.delete_all_wrong"))
            return

        for p in self._config.list_presets():
            self._config.remove_preset(p["id"])
        self._refresh_list(self._search.text())

    def _on_export_dialog(self):
        presets = self._config.list_presets()
        if not presets:
            QMessageBox.information(self, tr("dlg.export_title"), tr("dlg.import_empty"))
            return
        dialog = ExportPresetsDialog(presets, self)
        if dialog.exec() != QDialog.Accepted:
            return
        indices = dialog.get_selected_indices()
        if not indices:
            QMessageBox.information(self, tr("dlg.export_title"), tr("dlg.export_none"))
            return
        path, _ = QFileDialog.getSaveFileName(
            self,
            tr("dlg.export_title"),
            "presets.yaml",
            tr("filter.preset_yaml"),
        )
        if path:
            ids = [presets[i]["id"] for i in indices]
            count = self._config.export_presets_to_file(path, ids)
            QMessageBox.information(
                self, tr("dlg.export_title"), tr("dlg.export_count").format(count)
            )

    def _on_import_presets(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            tr("dlg.import_title"),
            "",
            tr("filter.preset_yaml"),
        )
        if not path:
            return
        try:
            imported = Config.read_presets_from_file(path)
        except (ValueError, OSError) as e:
            QMessageBox.critical(self, tr("dlg.import_error"), str(e))
            return
        if not imported:
            QMessageBox.information(self, tr("dlg.import_title"), tr("dlg.import_empty"))
            return

        dialog = ImportPresetsDialog(imported, self)
        if dialog.exec() != QDialog.Accepted:
            return

        indices = dialog.get_selected_indices()
        count = 0
        for i in indices:
            if len(self._config.list_presets()) >= MAX_PRESETS:
                break
            p = imported[i]
            self._config.add_preset(p["name"], p["text"], p.get("params"))
            count += 1
        self._refresh_list(self._search.text())
        QMessageBox.information(
            self, tr("dlg.import_title"), tr("dlg.import_count").format(count)
        )

    def _on_load(self):
        item = self._list_widget.currentItem()
        if item:
            self.accept()


MAX_PRESETS = 50


class NewPresetDialog(QDialog):
    def __init__(self, config: Config, current_text: str, current_settings: dict, parent=None):
        super().__init__(parent)
        self._config = config
        self._current_text = current_text
        self.setWindowTitle(tr("presets.new_title"))
        self.setMinimumSize(600, 480)
        self.resize(650, 520)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        name_row = QHBoxLayout()
        name_row.addWidget(QLabel(tr("presets.name")))
        self._name_edit = QLineEdit()
        self._name_edit.setPlaceholderText(tr("presets.name_holder"))
        name_row.addWidget(self._name_edit, 1)
        layout.addLayout(name_row)

        layout.addWidget(QLabel(tr("presets.text_label")))
        self._editor = QPlainTextEdit()
        self._editor.setPlaceholderText(tr("presets.placeholder"))
        self._editor.setPlainText(current_text)
        layout.addWidget(self._editor, 1)

        settings_group = QGroupBox(tr("presets.params"))
        settings_layout = QHBoxLayout(settings_group)
        settings_layout.setSpacing(10)

        speed_col = QVBoxLayout()
        speed_col.addWidget(QLabel(tr("presets.speed_label")))
        self._speed_spin = QSpinBox()
        self._speed_spin.setRange(1, 200)
        self._speed_spin.setValue(current_settings.get("speed_cps", 50))
        self._speed_spin.setFixedWidth(70)
        self._speed_spin.setButtonSymbols(QSpinBox.NoButtons)
        speed_col.addWidget(self._speed_spin)
        settings_layout.addLayout(speed_col)

        # Delay
        delay_col = QVBoxLayout()
        delay_col.addWidget(QLabel(tr("presets.delay_label")))
        self._delay_spin = QSpinBox()
        self._delay_spin.setRange(0, 10)
        self._delay_spin.setValue(current_settings.get("start_delay", 3))
        self._delay_spin.setFixedWidth(70)
        self._delay_spin.setButtonSymbols(QSpinBox.NoButtons)
        delay_col.addWidget(self._delay_spin)
        settings_layout.addLayout(delay_col)

        # Mode
        mode_col = QVBoxLayout()
        mode_col.addWidget(QLabel(tr("presets.mode_label")))
        self._real_radio = QRadioButton(tr("presets.mode_char"))
        self._inst_radio = QRadioButton(tr("presets.mode_instant"))
        mode_group = QButtonGroup(self)
        mode_group.addButton(self._real_radio, 0)
        mode_group.addButton(self._inst_radio, 1)
        if current_settings.get("mode", "realistic") == "instant":
            self._inst_radio.setChecked(True)
        else:
            self._real_radio.setChecked(True)
        self._inst_radio.toggled.connect(self._on_mode_toggled)
        mode_col.addWidget(self._real_radio)
        mode_col.addWidget(self._inst_radio)
        settings_layout.addLayout(mode_col)

        # Variance
        self._var_label = QLabel(tr("presets.variance_label"))
        self._var_spin = QSpinBox()
        self._var_spin.setRange(0, 50)
        self._var_spin.setValue(current_settings.get("variance_percent", 15))
        self._var_spin.setFixedWidth(70)
        self._var_spin.setButtonSymbols(QSpinBox.NoButtons)
        var_col = QVBoxLayout()
        var_col.addWidget(self._var_label)
        var_col.addWidget(self._var_spin)
        settings_layout.addLayout(var_col)

        settings_layout.addStretch()
        layout.addWidget(settings_group)

        self._on_mode_toggled()

        # Buttons
        btn_box = QDialogButtonBox()
        save_btn = btn_box.addButton(tr("btn.save_preset"), QDialogButtonBox.AcceptRole)
        save_btn.setObjectName("primaryBtn")
        btn_box.addButton(tr("btn.cancel"), QDialogButtonBox.RejectRole)
        btn_box.accepted.connect(self._on_save)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)

    def _on_mode_toggled(self):
        visible = not self._inst_radio.isChecked()
        self._var_label.setVisible(visible)
        self._var_spin.setVisible(visible)

    def _on_save(self):
        name = self._name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, tr("dlg.empty_name"), tr("dlg.enter_name"))
            return

        text = self._editor.toPlainText()

        if len(self._config.list_presets()) >= MAX_PRESETS:
            QMessageBox.warning(
                self, tr("dlg.limit_reached"), tr("dlg.limit_msg").format(MAX_PRESETS)
            )
            return

        params = {
            "speed_cps": self._speed_spin.value(),
            "start_delay": self._delay_spin.value(),
            "mode": "instant" if self._inst_radio.isChecked() else "realistic",
            "variance_percent": self._var_spin.value(),
        }
        self._config.add_preset(name, text, params)
        self.accept()

    def get_preset_name(self) -> str:
        return self._name_edit.text().strip()


class ImportPresetsDialog(QDialog):
    def __init__(self, presets: list[dict], parent=None):
        super().__init__(parent)
        self._presets = presets
        self._checks: list[QCheckBox] = []

        self.setWindowTitle(tr("dlg.import_title"))
        self.setMinimumSize(500, 380)
        self.resize(550, 450)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        layout.addWidget(SectionTitle(tr("dlg.import_title")))

        # Select all
        top_row = QHBoxLayout()
        self._select_all_cb = QCheckBox(tr("btn.select_all"))
        self._select_all_cb.setTristate(False)
        self._select_all_cb.toggled.connect(self._on_select_all)
        top_row.addWidget(self._select_all_cb)
        top_row.addStretch()
        layout.addLayout(top_row)

        # Scrollable preset list
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(4)

        for preset in presets:
            cb = QCheckBox(preset["name"])
            cb.setChecked(True)
            cb.setToolTip(preset["text"][:200])
            scroll_layout.addWidget(cb)
            self._checks.append(cb)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll, 1)

        # Buttons
        btn_box = QDialogButtonBox()
        import_btn = btn_box.addButton(tr("btn.import_selected"), QDialogButtonBox.AcceptRole)
        import_btn.setObjectName("primaryBtn")
        btn_box.addButton(tr("btn.cancel"), QDialogButtonBox.RejectRole)
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)

    def _on_select_all(self, checked: bool):
        text = tr("btn.deselect_all") if checked else tr("btn.select_all")
        self._select_all_cb.setText(text)
        for cb in self._checks:
            cb.setChecked(checked)

    def get_selected_indices(self) -> list[int]:
        return [i for i, cb in enumerate(self._checks) if cb.isChecked()]


class ExportPresetsDialog(QDialog):
    def __init__(self, presets: list[dict], parent=None):
        super().__init__(parent)
        self._presets = presets
        self._checks: list[QCheckBox] = []

        self.setWindowTitle(tr("dlg.export_title"))
        self.setMinimumSize(500, 380)
        self.resize(550, 450)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        layout.addWidget(SectionTitle(tr("dlg.export_title")))

        top_row = QHBoxLayout()
        self._select_all_cb = QCheckBox(tr("btn.select_all"))
        self._select_all_cb.setTristate(False)
        self._select_all_cb.toggled.connect(self._on_select_all)
        top_row.addWidget(self._select_all_cb)
        top_row.addStretch()
        layout.addLayout(top_row)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(4)

        for preset in presets:
            cb = QCheckBox(preset["name"])
            cb.setChecked(True)
            cb.setToolTip(preset["text"][:200])
            scroll_layout.addWidget(cb)
            self._checks.append(cb)

        scroll_layout.addStretch()
        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll, 1)

        btn_box = QDialogButtonBox()
        export_btn = btn_box.addButton(tr("btn.export"), QDialogButtonBox.AcceptRole)
        export_btn.setObjectName("primaryBtn")
        btn_box.addButton(tr("btn.cancel"), QDialogButtonBox.RejectRole)
        btn_box.accepted.connect(self.accept)
        btn_box.rejected.connect(self.reject)
        layout.addWidget(btn_box)

    def _on_select_all(self, checked: bool):
        text = tr("btn.deselect_all") if checked else tr("btn.select_all")
        self._select_all_cb.setText(text)
        for cb in self._checks:
            cb.setChecked(checked)

    def get_selected_indices(self) -> list[int]:
        return [i for i, cb in enumerate(self._checks) if cb.isChecked()]

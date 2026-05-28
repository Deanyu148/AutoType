from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QSizePolicy,
    QWidget,
    QLabel,
    QRadioButton,
    QButtonGroup,
    QCheckBox,
    QComboBox,
    QSpinBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
)

from src.ui.widgets import LabeledSlider, SectionTitle, CardFrame
from src.ui.theme import TEXT_SECONDARY
from src.utils.config import Config
from src.utils.i18n import tr, get_language, LANGUAGES


class SettingsPanel(CardFrame):
    settings_changed = Signal()
    language_changed = Signal(str)

    def __init__(self, config: Config, parent=None):
        super().__init__(parent)
        self._config = config
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setMinimumHeight(340)
        self.card_layout.setSpacing(10)

        self._title = SectionTitle(tr("section.settings"))
        self.addWidget(self._title)

        # Speed slider
        self._speed_slider = LabeledSlider(
            tr("settings.speed"),
            minimum=1, maximum=200,
            default=config.speed_cps,
            suffix=tr("unit.cps"),
            tooltip=tr("settings.speed_tip"),
        )
        self._speed_slider.value_changed.connect(self._emit_changed)
        self.addWidget(self._speed_slider)

        # Start delay slider
        self._delay_slider = LabeledSlider(
            tr("settings.delay"), minimum=0, maximum=10,
            default=config.start_delay, suffix=tr("unit.sec"),
        )
        self._delay_slider.value_changed.connect(self._emit_changed)
        self.addWidget(self._delay_slider)

        # Mode group
        self._mode_group = QGroupBox(tr("settings.mode_group"))
        self._mode_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self._mode_group.setMinimumHeight(56)
        mode_layout = QVBoxLayout(self._mode_group)
        mode_layout.setSpacing(6)

        self._realistic_radio = QRadioButton(tr("settings.mode_real"))
        self._instant_radio = QRadioButton(tr("settings.mode_instant"))
        mode_layout.addWidget(self._realistic_radio)
        mode_layout.addWidget(self._instant_radio)

        self._mode_btn_group = QButtonGroup(self)
        self._mode_btn_group.addButton(self._realistic_radio, 0)
        self._mode_btn_group.addButton(self._instant_radio, 1)

        if config.typing_mode == "instant":
            self._instant_radio.setChecked(True)
        else:
            self._realistic_radio.setChecked(True)

        self.addWidget(self._mode_group)

        # Variance slider
        self._variance_slider = LabeledSlider(
            tr("settings.variance"),
            minimum=0, maximum=50,
            default=config.variance_percent,
            suffix=tr("unit.pct"),
            tooltip=tr("settings.variance_tip"),
        )
        self._variance_slider.value_changed.connect(self._emit_changed)
        self.addWidget(self._variance_slider)

        self._realistic_radio.toggled.connect(self._on_mode_toggled)
        self._on_mode_toggled()

        # Always on top
        self._always_on_top_cb = QCheckBox(tr("settings.always_on_top"))
        self._always_on_top_cb.setChecked(config.always_on_top)
        self._always_on_top_cb.toggled.connect(self._emit_changed)
        self.addWidget(self._always_on_top_cb)

        # Language selector
        lang_row = QHBoxLayout()
        lang_row.setContentsMargins(0, 4, 0, 0)
        lang_row.addWidget(QLabel("语言/Language:"))
        self._lang_combo = QComboBox()
        self._lang_combo.setMinimumWidth(150)
        for code, name in LANGUAGES.items():
            self._lang_combo.addItem(name, code)
        self._lang_combo.currentIndexChanged.connect(
            lambda: self.language_changed.emit(self._lang_combo.currentData())
        )
        lang_row.addWidget(self._lang_combo)
        lang_row.addStretch()
        self.addLayout(lang_row)
        self._update_lang_combo()

    def _update_lang_combo(self):
        cur = get_language()
        for i in range(self._lang_combo.count()):
            if self._lang_combo.itemData(i) == cur:
                self._lang_combo.setCurrentIndex(i)
                break

    def retranslate_ui(self):
        self._title.setText(tr("section.settings"))
        self._speed_slider._label.setText(tr("settings.speed"))
        self._speed_slider._slider.setToolTip(tr("settings.speed_tip"))
        self._speed_slider._spin.setToolTip(tr("settings.speed_tip"))
        self._delay_slider._label.setText(tr("settings.delay"))
        self._mode_group.setTitle(tr("settings.mode_group"))
        self._realistic_radio.setText(tr("settings.mode_real"))
        self._instant_radio.setText(tr("settings.mode_instant"))
        self._variance_slider._label.setText(tr("settings.variance"))
        self._variance_slider._slider.setToolTip(tr("settings.variance_tip"))
        self._variance_slider._spin.setToolTip(tr("settings.variance_tip"))
        self._always_on_top_cb.setText(tr("settings.always_on_top"))
        self._update_lang_combo()

    def _on_mode_toggled(self):
        self._variance_slider.setVisible(self._realistic_radio.isChecked())

    def _emit_changed(self, *_):
        self.settings_changed.emit()

    def get_speed_cps(self) -> int:
        return self._speed_slider.value()

    def get_start_delay(self) -> int:
        return self._delay_slider.value()

    def get_mode(self) -> str:
        return "instant" if self._instant_radio.isChecked() else "realistic"

    def get_variance(self) -> int:
        return self._variance_slider.value()

    def apply_params(self, params: dict) -> None:
        if "speed_cps" in params:
            self._speed_slider.setValue(params["speed_cps"])
        if "start_delay" in params:
            self._delay_slider.setValue(params["start_delay"])
        if "mode" in params:
            if params["mode"] == "instant":
                self._instant_radio.setChecked(True)
            else:
                self._realistic_radio.setChecked(True)
        if "variance_percent" in params:
            self._variance_slider.setValue(params["variance_percent"])

    def is_always_on_top(self) -> bool:
        return self._always_on_top_cb.isChecked()

    def save_to_config(self):
        self._config.speed_cps = self.get_speed_cps()
        self._config.start_delay = self.get_start_delay()
        self._config.typing_mode = self.get_mode()
        self._config.variance_percent = self.get_variance()
        self._config.always_on_top = self.is_always_on_top()

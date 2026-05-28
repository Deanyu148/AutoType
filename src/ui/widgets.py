from PySide6.QtCore import Qt, Signal, QSize, QPoint, QRect, QPropertyAnimation
from PySide6.QtGui import QPainter, QColor, QFont, QIcon
from PySide6.QtWidgets import (
    QSizePolicy,
    QWidget,
    QLabel,
    QSlider,
    QSpinBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QGraphicsOpacityEffect,
)

from src.ui.theme import (
    BG_DARK,
    BG_SURFACE,
    BG_INPUT,
    PRIMARY,
    PRIMARY_HOVER,
    ACCENT,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    SUCCESS,
    WARNING,
    ERROR,
    BORDER_STRONG,
)
from src.utils.i18n import tr as _tr


class CardFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)
        self.card_layout = layout

    def addWidget(self, widget: QWidget, stretch: int = 0):
        self.card_layout.addWidget(widget, stretch)

    def addLayout(self, layout, stretch: int = 0):
        self.card_layout.addLayout(layout, stretch)


class SectionTitle(QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName("sectionTitle")


class LabeledSlider(QWidget):
    value_changed = Signal(int)

    def __init__(
        self,
        label: str,
        minimum: int = 1,
        maximum: int = 200,
        default: int = 50,
        suffix: str = "",
        tooltip: str = "",
        parent=None,
    ):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setMinimumHeight(46)
        self._suffix = suffix
        self._updating = False

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 2, 0, 2)
        layout.setSpacing(4)

        header = QHBoxLayout()
        header.setContentsMargins(0, 0, 0, 0)

        self._label = QLabel(label)
        self._label.setStyleSheet(f"color: {TEXT_SECONDARY}; font-size: 12px;")
        header.addWidget(self._label)

        header.addStretch()
        layout.addLayout(header)

        row = QHBoxLayout()
        row.setContentsMargins(0, 0, 0, 0)
        row.setSpacing(8)

        self._slider = QSlider(Qt.Horizontal)
        self._slider.setMinimum(minimum)
        self._slider.setMaximum(maximum)
        self._slider.setValue(default)
        self._slider.valueChanged.connect(self._on_slider_changed)
        if tooltip:
            self._slider.setToolTip(tooltip)
        row.addWidget(self._slider, 1)

        self._spin = QSpinBox()
        self._spin.setMinimum(minimum)
        self._spin.setMaximum(maximum)
        self._spin.setValue(default)
        self._spin.setFixedWidth(60)
        self._spin.setButtonSymbols(QSpinBox.NoButtons)
        self._spin.valueChanged.connect(self._on_spin_changed)
        self._spin.setToolTip(tooltip)
        row.addWidget(self._spin)

        if suffix:
            suffix_label = QLabel(suffix)
            suffix_label.setStyleSheet(
                f"color: {TEXT_SECONDARY}; font-size: 11px; padding-left: 2px;"
            )
            row.addWidget(suffix_label)

        layout.addLayout(row)

    def _on_slider_changed(self, value: int):
        if self._updating:
            return
        self._updating = True
        self._spin.setValue(value)
        self._updating = False
        self.value_changed.emit(value)

    def _on_spin_changed(self, value: int):
        if self._updating:
            return
        self._updating = True
        self._slider.setValue(value)
        self._updating = False
        self.value_changed.emit(value)

    def value(self) -> int:
        return self._spin.value()

    def setValue(self, value: int):
        self._spin.setValue(value)


class StatusIndicator(QWidget):
    STATUS_COLORS = {
        "ready": SUCCESS,
        "countdown": WARNING,
        "typing": PRIMARY,
        "paused": WARNING,
        "complete": SUCCESS,
        "error": ERROR,
    }

    def __init__(self, show_label: bool = True, parent=None):
        super().__init__(parent)
        self._status = "ready"
        self._show_label = show_label
        self._pulse_alpha = 1.0
        self._pulse_timer = None

    def set_status(self, status: str):
        self._status = status
        if status == "typing":
            self._start_pulse()
        else:
            self._stop_pulse()
        self.update()

    def _start_pulse(self):
        if not self._pulse_timer:
            from PySide6.QtCore import QTimer

            self._pulse_timer = QTimer(self)
            self._pulse_timer.timeout.connect(self._on_pulse)
            self._pulse_step = -0.03
            self._pulse_timer.start(30)

    def _stop_pulse(self):
        if self._pulse_timer:
            self._pulse_timer.stop()
            self._pulse_timer = None
        self._pulse_alpha = 1.0

    def _on_pulse(self):
        self._pulse_alpha += self._pulse_step
        if self._pulse_alpha <= 0.4 or self._pulse_alpha >= 1.0:
            self._pulse_step = -self._pulse_step
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)

        dot_color = QColor(self.STATUS_COLORS.get(self._status, TEXT_SECONDARY))
        dot_color.setAlphaF(self._pulse_alpha)

        dot_radius = 5
        dot_x = 2
        dot_y = self.height() // 2 - dot_radius
        painter.setPen(Qt.NoPen)
        painter.setBrush(dot_color)
        painter.drawEllipse(QPoint(dot_x + dot_radius, dot_y + dot_radius), dot_radius, dot_radius)

        if self._show_label:
            label = _tr(f"state.{self._status}")
            painter.setPen(QColor(TEXT_PRIMARY))
            font = QFont(self.font())
            font.setPointSize(10)
            painter.setFont(font)
            text_x = dot_x + dot_radius * 2 + 8
            painter.drawText(
                QRect(text_x, 0, self.width() - text_x, self.height()),
                Qt.AlignVCenter | Qt.AlignLeft,
                label,
            )

    def sizeHint(self):
        return self.minimumSizeHint()

    def minimumSizeHint(self):
        if self._show_label:
            return self._size_hint_with_label()
        return self._size_hint_dot_only()

    def _size_hint_with_label(self):
        return QSize(120, 22)

    def _size_hint_dot_only(self):
        return QSize(14, 14)


class HotkeyLabel(QLabel):
    def __init__(self, key: str, parent=None):
        super().__init__(key.upper(), parent)
        self.setObjectName("hotkeyLabel")


class CountdownOverlay(QWidget):
    cancelled = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.hide()
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self._current_number = 0

    def show_countdown(self, number: int):
        self._current_number = number
        self.setGeometry(self.parent().rect())
        self.raise_()
        self.show()
        self.update()

    def hide_overlay(self):
        self.hide()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.fillRect(self.rect(), QColor(0, 0, 0, 170))

        if self._current_number > 0:
            painter.setPen(QColor("#ffffff"))
            painter.setFont(QFont("Segoe UI", 96, QFont.Bold))
            painter.drawText(self.rect(), Qt.AlignCenter, str(self._current_number))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.cancelled.emit()
            self.hide_overlay()
        super().keyPressEvent(event)

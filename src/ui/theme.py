from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

# ── Color Palette (Catppuccin Mocha inspired) ─────────────────

BG_DARK = "#1a1b26"
BG_SURFACE = "#24253a"
BG_HOVER = "#313352"
BG_INPUT = "#1a1b2e"
PRIMARY = "#7c3aed"
PRIMARY_HOVER = "#9d6ff7"
ACCENT = "#a78bfa"
TEXT_PRIMARY = "#cdd6f4"
TEXT_SECONDARY = "#9399b2"
TEXT_MUTED = "#6c7086"
SUCCESS = "#10b981"
WARNING = "#f59e0b"
ERROR = "#ef4444"
ERROR_HOVER = "#f87171"
BORDER = "#363852"
BORDER_STRONG = "#45475a"

DARK_THEME_QSS = r"""
/* ── Global Reset ───────────────────────────────── */

* {
    font-family: "Microsoft YaHei", "Segoe UI", "Helvetica Neue", Arial, sans-serif;
    color: #cdd6f4;
    selection-background-color: #7c3aed;
    selection-color: #ffffff;
    font-style: normal;
}

QMainWindow {
    background-color: #1a1b26;
}

QMenuBar {
    background-color: #1a1b26;
    border-bottom: 1px solid #24253a;
    padding: 2px 0;
    font-size: 13px;
}

QMenuBar::item {
    padding: 4px 12px;
    border-radius: 4px;
    margin: 2px 4px;
    background: transparent;
}

QMenuBar::item:selected {
    background-color: #313352;
}

QMenu {
    background-color: #24253a;
    border: 1px solid #363852;
    border-radius: 6px;
    padding: 4px;
}

QMenu::item {
    padding: 6px 28px 6px 12px;
    border-radius: 4px;
    font-size: 13px;
}

QMenu::item:selected {
    background-color: #313352;
}

QMenu::separator {
    height: 1px;
    background: #363852;
    margin: 4px 8px;
}

/* ── Status Bar ─────────────────────────────────── */

QStatusBar {
    background-color: #12131f;
    border-top: 1px solid #24253a;
    padding: 3px 8px;
    font-size: 12px;
    color: #9399b2;
}

QStatusBar QLabel {
    color: #9399b2;
}

/* ── Scroll Area ────────────────────────────────── */

QScrollArea {
    border: none;
    background: transparent;
}

QScrollArea > QWidget > QWidget {
    background: transparent;
}

QScrollBar:vertical {
    background: transparent;
    width: 8px;
    margin: 2px;
}

QScrollBar::handle:vertical {
    background: #363852;
    border-radius: 4px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: #45475a;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: transparent;
}

QScrollBar:horizontal {
    background: transparent;
    height: 8px;
    margin: 2px;
}

QScrollBar::handle:horizontal {
    background: #363852;
    border-radius: 4px;
    min-width: 30px;
}

QScrollBar::handle:horizontal:hover {
    background: #45475a;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0;
}

/* ── Buttons ────────────────────────────────────── */

QPushButton {
    background-color: #313352;
    color: #cdd6f4;
    border: 1px solid #363852;
    border-radius: 6px;
    padding: 5px 14px;
    font-size: 12px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #3d3d64;
    border-color: #45475a;
}

QPushButton:pressed {
    background-color: #24253a;
}

QPushButton:disabled {
    background-color: #24253a;
    color: #6c7086;
    border-color: #363852;
}

QPushButton#primaryBtn {
    background-color: #7c3aed;
    border: 1px solid #7c3aed;
    color: #ffffff;
    font-weight: 600;
}

QPushButton#primaryBtn:hover {
    background-color: #9d6ff7;
    border-color: #9d6ff7;
}

QPushButton#primaryBtn:pressed {
    background-color: #6d28d9;
}

QPushButton#primaryBtn:disabled {
    background-color: #5b3a8c;
    border-color: #5b3a8c;
    color: #a0a0c0;
}

QPushButton#stopBtn {
    background-color: #ef4444;
    border: 1px solid #ef4444;
    color: #ffffff;
    font-weight: 600;
}

QPushButton#stopBtn:hover {
    background-color: #f87171;
    border-color: #f87171;
}

QPushButton#stopBtn:pressed {
    background-color: #dc2626;
}

QPushButton#stopBtn:disabled {
    background-color: #7a3434;
    border-color: #7a3434;
    color: #a0a0c0;
}

QPushButton#secondaryBtn {
    background-color: transparent;
    border: 1px solid #45475a;
}

QPushButton#secondaryBtn:hover {
    background-color: #313352;
    border-color: #7c3aed;
}

QPushButton#dangerBtn {
    background-color: transparent;
    border: 1px solid #7a3434;
    color: #ef4444;
}

QPushButton#dangerBtn:hover {
    background-color: #7a3434;
    color: #ffffff;
}

/* ── Text Editor ────────────────────────────────── */

QPlainTextEdit {
    background-color: #1a1b2e;
    border: 1px solid #363852;
    border-radius: 6px;
    padding: 10px;
    font-family: "Cascadia Code", "Fira Code", "JetBrains Mono", "Consolas", monospace;
    font-size: 14px;
    color: #cdd6f4;
}

QPlainTextEdit:focus {
    border-color: #7c3aed;
}

QLineEdit {
    background-color: #1a1b2e;
    border: 1px solid #363852;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 13px;
    color: #cdd6f4;
}

QLineEdit:focus {
    border-color: #7c3aed;
}

/* ── Sliders ────────────────────────────────────── */

QSlider::groove:horizontal {
    background: #1a1b2e;
    height: 6px;
    border-radius: 3px;
    border: 1px solid #363852;
}

QSlider::sub-page:horizontal {
    background: #7c3aed;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #7c3aed;
    border: 1px solid #cdd6f4;
    width: 10px;
    height: 10px;
    margin: -3px 0;
    border-radius: 5px;
}

QSlider::handle:horizontal:hover {
    background: #9d6ff7;
    border-color: #ffffff;
}

/* ── Check Boxes & Radio Buttons ────────────────── */

QCheckBox {
    spacing: 6px;
    font-size: 12px;
    color: #cdd6f4;
}

QCheckBox::indicator {
    width: 14px;
    height: 14px;
    border: 1.5px solid #45475a;
    border-radius: 3px;
    background: transparent;
}

QCheckBox::indicator:hover {
    border-color: #7c3aed;
}

QCheckBox::indicator:checked {
    background: #7c3aed;
    border-color: #7c3aed;
}

QRadioButton {
    spacing: 6px;
    font-size: 12px;
    color: #cdd6f4;
}

QRadioButton::indicator {
    width: 14px;
    height: 14px;
    border: 1.5px solid #45475a;
    border-radius: 7px;
    background: transparent;
}

QRadioButton::indicator:hover {
    border-color: #7c3aed;
}

QRadioButton::indicator:checked {
    background: #7c3aed;
    border-color: #7c3aed;
}

/* ── Combo Box ──────────────────────────────────── */

QComboBox {
    background-color: #1a1b2e;
    border: 1px solid #363852;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 13px;
    color: #cdd6f4;
    min-width: 120px;
}

QComboBox:hover {
    border-color: #45475a;
}

QComboBox:focus {
    border-color: #7c3aed;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 28px;
    border-left: 1px solid #363852;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    background: #24253a;
}

QComboBox QAbstractItemView {
    background-color: #24253a;
    border: 1px solid #363852;
    border-radius: 4px;
    selection-background-color: #313352;
    selection-color: #cdd6f4;
    outline: none;
    padding: 4px;
}

QComboBox QAbstractItemView::item {
    padding: 5px 10px;
    border-radius: 4px;
}

/* ── Progress Bar ───────────────────────────────── */

QProgressBar {
    background-color: #1a1b2e;
    border: 1px solid #363852;
    border-radius: 6px;
    height: 18px;
    text-align: center;
    font-size: 11px;
    color: #cdd6f4;
}

QProgressBar::chunk {
    background-color: #7c3aed;
    border-radius: 5px;
}

/* ── Spin Box ───────────────────────────────────── */

QSpinBox {
    background-color: #1a1b2e;
    border: 1px solid #363852;
    border-radius: 6px;
    padding: 6px 10px;
    font-size: 13px;
    color: #cdd6f4;
}

QSpinBox:focus {
    border-color: #7c3aed;
}

QSpinBox::up-button, QSpinBox::down-button {
    width: 24px;
    border: none;
    background: #24253a;
}

QSpinBox::up-button:hover, QSpinBox::down-button:hover {
    background: #313352;
}

/* ── Group Box ──────────────────────────────────── */

QGroupBox {
    font-size: 12px;
    font-weight: 500;
    color: #9399b2;
    border: 1px solid #363852;
    border-radius: 6px;
    margin-top: 8px;
    padding: 10px 8px 6px 8px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
    color: #a78bfa;
}

/* ── Tool Tips ──────────────────────────────────── */

QToolTip {
    background-color: #24253a;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 4px;
    padding: 5px 10px;
    font-size: 12px;
}

/* ── Dialogs ────────────────────────────────────── */

QDialog {
    background-color: #1a1b26;
}

QLabel#sectionTitle {
    color: #a78bfa;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 0;
    margin: 0;
}

QLabel#hotkeyLabel {
    background-color: #1a1b2e;
    color: #a78bfa;
    border: 1px solid #45475a;
    border-radius: 3px;
    padding: 1px 4px;
    font-size: 10px;
    font-weight: 600;
    font-family: "Consolas", monospace;
}

/* ── Card Frame ─────────────────────────────────── */

QFrame#card {
    background: #24253a;
    border: 1px solid #363852;
    border-radius: 10px;
    padding: 10px;
}

QFrame#card:hover {
    border-color: #45475a;
}

/* ── List Widget ────────────────────────────────── */

QListWidget {
    background-color: #1a1b2e;
    border: 1px solid #363852;
    border-radius: 6px;
    outline: none;
    font-size: 13px;
}

QListWidget::item {
    padding: 6px 10px;
    border-radius: 4px;
    color: #cdd6f4;
}

QListWidget::item:selected {
    background-color: #7c3aed;
    color: #ffffff;
}

QListWidget::item:hover {
    background-color: #313352;
}
"""


def apply_theme(app: QApplication) -> None:
    app.setStyle("Fusion")
    app.setStyleSheet(DARK_THEME_QSS)

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(BG_DARK))
    palette.setColor(QPalette.WindowText, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.Base, QColor(BG_INPUT))
    palette.setColor(QPalette.Text, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.Button, QColor(BG_SURFACE))
    palette.setColor(QPalette.ButtonText, QColor(TEXT_PRIMARY))
    palette.setColor(QPalette.Highlight, QColor(PRIMARY))
    palette.setColor(QPalette.HighlightedText, QColor("#ffffff"))
    palette.setColor(QPalette.Disabled, QPalette.Text, QColor(TEXT_MUTED))
    palette.setColor(QPalette.Disabled, QPalette.ButtonText, QColor(TEXT_MUTED))
    app.setPalette(palette)

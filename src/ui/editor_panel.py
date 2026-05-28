from PySide6.QtCore import Qt, Signal, QRect
from PySide6.QtGui import QPainter, QColor, QFont, QFontDatabase, QTextFormat
from PySide6.QtWidgets import (
    QWidget,
    QPlainTextEdit,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)

from src.ui.theme import BG_DARK, BG_SURFACE, TEXT_SECONDARY, TEXT_MUTED, BORDER
from src.utils.i18n import tr


class _LineNumberArea(QWidget):
    def __init__(self, editor: "EditorPanel"):
        super().__init__(editor)
        self._editor = editor

    def sizeHint(self):
        return self._editor._line_number_size()

    def paintEvent(self, event):
        self._editor._paint_line_numbers(event)


class EditorPanel(QFrame):
    text_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("editor")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        self._title = QLabel(tr("section.text_input"))
        self._title.setObjectName("sectionTitle")
        layout.addWidget(self._title)

        self._edit = QPlainTextEdit()
        self._edit.setPlaceholderText(tr("editor.placeholder"))
        self._edit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        self._edit.setTabStopDistance(28)

        editor_font = QFont("Consolas", 12)
        editor_font.setStyleHint(QFont.Monospace)
        self._edit.setFont(editor_font)
        self._edit.textChanged.connect(self._on_text_changed)
        self._edit.blockCountChanged.connect(self._update_line_number_width)
        self._edit.updateRequest.connect(self._update_line_numbers)

        layout.addWidget(self._edit, 1)

        self._line_number_area = _LineNumberArea(self)
        self._line_number_area.show()
        self._line_number_area.raise_()

        self._line_count = self._edit.document().blockCount()
        self._edit.setViewportMargins(self._line_number_area_width(), 0, 0, 0)

        footer = QHBoxLayout()
        footer.setContentsMargins(4, 0, 4, 0)

        self._char_count_label = QLabel()
        self._char_count_label.setStyleSheet(
            f"color: {TEXT_MUTED}; font-size: 11px;"
        )
        self._word_count_label = QLabel()
        self._word_count_label.setStyleSheet(
            f"color: {TEXT_MUTED}; font-size: 11px;"
        )
        self._line_count_label = QLabel()
        self._line_count_label.setStyleSheet(
            f"color: {TEXT_MUTED}; font-size: 11px;"
        )

        footer.addWidget(self._char_count_label)
        footer.addWidget(self._word_count_label)
        footer.addWidget(self._line_count_label)
        footer.addStretch()

        self._clear_btn = QPushButton(tr("btn.clear"))
        self._clear_btn.setObjectName("secondaryBtn")
        self._clear_btn.setFixedHeight(22)
        self._clear_btn.setMinimumWidth(50)
        self._clear_btn.clicked.connect(lambda: self._edit.clear())
        footer.addWidget(self._clear_btn)

        layout.addLayout(footer)

        self._update_counts()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self._edit.contentsRect()
        width = self._line_number_area_width()
        offset = self._edit.pos()
        self._line_number_area.setGeometry(
            QRect(cr.left() + 4 + offset.x(), cr.top() + offset.y(), width, cr.height())
        )

    def _line_number_area_width(self) -> int:
        digits = max(1, len(str(self._edit.blockCount())))
        space = 8 + self._edit.fontMetrics().horizontalAdvance("0") * (digits + 1)
        return space

    def _line_number_size(self):
        return self._line_number_area.sizeHint()

    def _update_line_number_width(self):
        new_count = self._edit.document().blockCount()
        if new_count != self._line_count:
            digits = max(1, len(str(new_count)))
            self._edit.setViewportMargins(
                self._line_number_area_width(), 0, 0, 0
            )
            self._line_count = new_count

    def _update_line_numbers(self, rect, dy):
        if dy:
            self._line_number_area.scroll(0, dy)
        else:
            self._line_number_area.update(
                0, rect.y(), self._line_number_area.width(), rect.height()
            )
        if rect.contains(self._edit.viewport().rect()):
            self._update_line_number_width()

    def _paint_line_numbers(self, event):
        painter = QPainter(self._line_number_area)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.fillRect(event.rect(), QColor(BG_DARK))

        block = self._edit.firstVisibleBlock()
        block_number = block.blockNumber()
        top = int(
            self._edit.blockBoundingGeometry(block)
            .translated(self._edit.contentOffset())
            .top()
        )
        bottom = top + int(self._edit.blockBoundingRect(block).height())
        width = self._line_number_area.width() - 4

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(QColor(TEXT_MUTED))
                painter.setFont(QFont("Consolas", 11))
                painter.drawText(
                    0, top, width, self._edit.fontMetrics().height(),
                    Qt.AlignRight, number
                )
            block = block.next()
            top = bottom
            bottom = top + int(self._edit.blockBoundingRect(block).height())
            block_number += 1

    def _on_text_changed(self):
        self._update_counts()
        self.text_changed.emit()

    def _update_counts(self):
        text = self._edit.toPlainText()
        blocks = self._edit.document().blockCount()
        lines = 0 if blocks == 1 and not text else blocks
        visible_text = text.replace("\r\n", "").replace("\n", "").replace("\r", "").replace("\t", "")
        chars = len(visible_text)
        self._char_count_label.setText(f"{tr('editor.chars')}: {chars}")
        if self._is_cjk_text(text):
            words = chars
        else:
            words = len(text.split()) if text else 0
        self._word_count_label.setText(f"{tr('editor.words')}: {words}")
        self._line_count_label.setText(f"{tr('editor.lines')}: {lines}")

    @staticmethod
    def _is_cjk_text(text: str) -> bool:
        for ch in text:
            cp = ord(ch)
            if 0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF or 0xF900 <= cp <= 0xFAFF:
                return True
        return False

    def get_text(self) -> str:
        return self._edit.toPlainText()

    def set_text(self, text: str):
        self._edit.setPlainText(text)

    def retranslate_ui(self):
        self._title.setText(tr("section.text_input"))
        self._edit.setPlaceholderText(tr("editor.placeholder"))
        self._clear_btn.setText(tr("btn.clear"))
        self._edit.viewport().update()
        self._update_counts()

    def is_empty(self) -> bool:
        return len(self._edit.toPlainText().strip()) == 0

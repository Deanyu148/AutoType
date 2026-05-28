import sys, os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMessageBox
from src.utils.config import Config
from src.utils.i18n import set_language, tr
from src.ui.theme import apply_theme
from src.ui.main_window import MainWindow


def _get_icon_path() -> str:
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "AutoType.ico")


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("AutoType")
    app.setOrganizationName("AutoType")
    app.setApplicationVersion("1.0.0")

    icon_path = _get_icon_path()
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    apply_theme(app)

    try:
        config = Config()
        config.load()
        set_language(config._data.get("language", "zh"))
    except Exception as e:
        QMessageBox.critical(None, tr("dlg.config_error"), tr("dlg.config_failed") + f":\n{e}")
        config = Config()

    window = MainWindow(config)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

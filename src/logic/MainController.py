import sys

from PyQt6.QtWidgets import QApplication
from src.logic import StyleSheetLoader
from src.ui.MainView import create_main_window


def setup():
    app = QApplication(sys.argv)

    StyleSheetLoader.load_stylesheet(app, "src/styles/styles.qss")
    
    window = create_main_window(app)
    window.show()

    sys.exit(app.exec())
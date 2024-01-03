import sys
from PyQt6.QtWidgets import QApplication
from src.logic import StyleSheetLoader
from src.ui.MainView import create_main_window

class MainController:
    def __init__(self):
        self.app = QApplication(sys.argv)

        StyleSheetLoader.load_stylesheet(self.app, "src/styles/styles.qss")
        self.window = create_main_window(self.app)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())

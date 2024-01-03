import sys
from PyQt6.QtWidgets import QApplication
from src.logic.UiLogic import UiLogic
from src.logic import StyleSheetLoader
from src.ui.MainView import create_main_window
from src.data.Data import Data


class MyApplication(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = Data()
        self.ui_logic = UiLogic()


class MainController:
    def __init__(self):
        self.app = MyApplication(sys.argv)

        self.data = Data()

        StyleSheetLoader.load_stylesheet(self.app, "src/styles/styles.qss")
        self.window = create_main_window(self.app)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec())

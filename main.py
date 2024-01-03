from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDockWidget, QVBoxLayout, QWidget, QStackedWidget
from src.logic import StyleSheetLoader
from src.ui.MainView import create_main_window
from src.logic.UiLogic import on_button_clicked


def start_app(on_button_clicked):
    app = QApplication([])
    StyleSheetLoader.load_stylesheet(app, "src/styles/styles.qss")
    window = create_main_window(app, on_button_clicked)
    window.show()
    app.exec()
    return app

if __name__ == "__main__":
    app = start_app(on_button_clicked)
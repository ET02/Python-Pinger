from PyQt6.QtWidgets import QApplication
from src.logic import SuperPinger

class UiLogic:
    def __init__(self):
        self.data = QApplication.instance().data

    def on_sidebar_button_clicked(self, idx):
        print(f"Button {idx} clicked!")

        if idx == 2:
            SuperPinger.ping_range(1, 25)
        if idx == 3:
            self.data.add_item("Hello")

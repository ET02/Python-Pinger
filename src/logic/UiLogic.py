from PyQt6.QtWidgets import QApplication
from src.logic.PingThread import PingThread
from src.logic.PingThread import handle_ping_result

class UiLogic:
    def __init__(self):
        self.data = QApplication.instance().data
        self.ping_thread = None

    def on_sidebar_button_clicked(self, idx):
        print(f"Button {idx} clicked!")

        if idx == 1:
            self.ping_thread = PingThread(230, 254)
            self.ping_thread.ping_result.connect(handle_ping_result)
            self.ping_thread.start()
        elif idx == 2:
            self.data.add_item("Muuh")
        elif idx == 3:
            self.data.add_item("Määäh")
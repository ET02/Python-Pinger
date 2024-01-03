from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from src.ui.pages.PingPage import PingPage


class PageContainer(QWidget):
    def __init__(self):
        super().__init__()

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Create a QStackedWidget
        self.pages = QStackedWidget()

        self.ping_page = PingPage("ping")
        self.nmap_page = PingPage("Nmap")

        self.pages.addWidget(self.ping_page)
        self.pages.addWidget(self.nmap_page)
        
        # Add the QStackedWidget to the layout
        layout.addWidget(self.pages)

        # Set the layout of the PageContainer
        self.setLayout(layout)

    def switch_page(self, page_name):
        if page_name == "Ping":
            self.pages.setCurrentWidget(self.ping_page)
        elif page_name == "Nmap":
            self.pages.setCurrentWidget(self.nmap_page)

# this file will contain the content of my main view of this python qt6 project. it will show multiple pages where only one will be active at a time. Implement a component in this class which willhold the main page. it will be initialized in another class. Make this class hold multiple pages in a data structure and make it be able to switch the current page.
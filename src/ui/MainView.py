from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QStackedWidget
from src.ui.SideBar import SideBar
from src.ui.PageContainer import PageContainer
from src.ui.pages.PingPage import PingPage


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.resize(800, 500)

        # Create a central widget and set it to the main window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Center the window
        screen = QApplication.primaryScreen()
        rect = screen.availableGeometry()
        center = rect.center()
        self.move(center.x() - self.width() // 2, center.y() - self.height() // 2)

        

        # Create an instance of SideBar and add it to the layout
        sidebar = SideBar()
        self.layout.addWidget(sidebar)
        sidebar.add_buttons()

        # Add the content widget to the layout
        page_container = PageContainer()
        self.layout.addWidget(page_container)
        page_container.switch_page("Ping")
        
def create_main_window(app):
    window = MainWindow(app)
    return window
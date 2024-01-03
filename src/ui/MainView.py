from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDockWidget, QVBoxLayout, QWidget, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from src.ui.SideBar import SideBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.resize(800, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Create the stacked widget
        self.stacked_widget = QStackedWidget()

        # Create some content for the stacked widget
        for i in range(5):
            button = QPushButton(f"Content {i}")
            self.stacked_widget.addWidget(button)

        # Add the stacked widget to the layout
        self.layout.addWidget(self.stacked_widget)




        # Create an instance of SideBar and add it to the layout
        sidebar = SideBar()
        self.layout.addWidget(sidebar)

        # Center the window
        screen = QApplication.primaryScreen()
        rect = screen.availableGeometry()
        center = rect.center()
        self.move(center.x() - self.width() // 2, center.y() - self.height() // 2)

def create_main_window(app):
    window = MainWindow(app)
    return window
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QDockWidget, QVBoxLayout, QWidget, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self, app, on_button_clicked):
        super().__init__()
        self.app = app
        self.resize(800, 500)

        # Create the stacked widget
        self.stacked_widget = QStackedWidget()

        # Create some content for the stacked widget
        for i in range(5):
            button = QPushButton(f"Content {i}")
            self.stacked_widget.addWidget(button)

        # Create the taskbar
        self.taskbar = QDockWidget("Taskbar")
        self.taskbar.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)  # disable all dockable features
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.taskbar)

        # Create some buttons for the taskbar
        taskbar_widget = QWidget()
        taskbar_layout = QVBoxLayout()
        for i in range(4):
            button = QPushButton()
            button.setIcon(QIcon(f"../../media/icons/icon{i}.png"))  # set the icon of the button
            button.clicked.connect(lambda i=i: self.stacked_widget.setCurrentIndex(i))
            taskbar_layout.addWidget(button)
        taskbar_widget.setLayout(taskbar_layout)
        self.taskbar.setWidget(taskbar_widget)

        # Set the stacked widget as the central widget
        self.setCentralWidget(self.stacked_widget)

        # Center the window
        screen = QApplication.primaryScreen()
        rect = screen.availableGeometry()
        center = rect.center()
        self.move(center.x() - self.width() // 2, center.y() - self.height() // 2)

def create_main_window(app, on_button_clicked):
    return MainWindow(app, on_button_clicked)
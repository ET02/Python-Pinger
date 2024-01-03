from PyQt6.QtWidgets import QWidget, QVBoxLayout, QToolButton
from src.logic.UiLogic import on_sidebar_button_clicked
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class SideBar(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # align the buttons to the top
        self.setLayout(self.layout)

        # Create some buttons for the taskbar
        # taskbar_widget = QWidget()
        # taskbar_layout = QVBoxLayout()
        # for i in range(4):
        #     button = QPushButton()
        #     button.setIcon(QIcon(f"../../media/icons/icon{i}.png"))  # set the icon of the button
        #     button.clicked.connect(lambda i=i: self.stacked_widget.setCurrentIndex(i))
        #     taskbar_layout.addWidget(button)
        # taskbar_widget.setLayout(taskbar_layout)
        # self.taskbar.setWidget(taskbar_widget)

    def add_button(self, name, icon_path, on_click):
        # Create the icon button
        icon = QToolButton()
        # set icon properties
        icon.setIcon(QIcon(icon_path))
        icon.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)  # display only the icon
        # set the tooltip text
        icon.setToolTip(name)
        # connect the button to the on_click function
        icon.clicked.connect(on_click)
        self.layout.addWidget(icon)

    def add_buttons(self):
        # Create the icon buttons
        self.add_button("Ping", "../../media/icons/icon1.png", lambda: on_sidebar_button_clicked(1))
        self.add_button("Nmap", "../../media/icons/icon2.png", lambda: on_sidebar_button_clicked(2))
        self.add_button("Go Buster", "../../media/icons/icon3.png", lambda: on_sidebar_button_clicked(3))
        
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QToolButton, QApplication
from src.logic.UiLogic import UiLogic
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import os


class SideBar(QWidget):
    def __init__(self):
        super().__init__()
        

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # align the buttons to the top
        self.setLayout(self.layout)

    def add_button(self, name, icon_path, on_click):
        # Create the icon button
        icon = QToolButton()

        project_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        full_icon_path = os.path.join(project_path, icon_path)
        print(full_icon_path)
        # set icon properties
        icon.setIcon(QIcon(full_icon_path))
        icon.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)  # display only the icon
        # set the tooltip text
        icon.setToolTip(name)
        # connect the button to the on_click function
        icon.clicked.connect(on_click)
        # set the icon size to the size of the button
        icon.setIconSize(icon.sizeHint())
        self.layout.addWidget(icon)

    def add_buttons(self):
        # Create the icon buttons
        self.add_button("Ping", "media/icons/icon0.png", lambda: QApplication.instance().ui_logic.on_sidebar_button_clicked(1))
        self.add_button("Nmap", "media/icons/icon2.png", lambda: QApplication.instance().ui_logic.on_sidebar_button_clicked(2))
        self.add_button("Go Buster", "media/icons/icon3.png", lambda: QApplication.instance().ui_logic.on_sidebar_button_clicked(3))
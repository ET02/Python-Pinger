from PyQt6.QtWidgets import QWidget, QVBoxLayout, QToolButton
from src.logic.UiLogic import on_sidebar_button_clicked

class SideBar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the icons
        icon1 = QToolButton()
        icon1.setText("Icon 1")
        icon1.clicked.connect(on_sidebar_button_clicked)
        layout.addWidget(icon1)

        icon2 = QToolButton()
        icon2.setText("Icon 2")
        icon2.clicked.connect(on_sidebar_button_clicked)
        layout.addWidget(icon2)

        icon3 = QToolButton()
        icon3.setText("Icon 3")
        icon3.clicked.connect(on_sidebar_button_clicked)
        layout.addWidget(icon3)

        icon4 = QToolButton()
        icon4.setText("Icon 4")
        icon4.clicked.connect(on_sidebar_button_clicked)
        layout.addWidget(icon4)


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
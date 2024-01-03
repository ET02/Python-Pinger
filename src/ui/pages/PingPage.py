from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem

class PingPage(QWidget):
    def __init__(self, name, items):
        super().__init__()
        self.name = name

        # Create a QVBoxLayout instance
        layout = QVBoxLayout()

        # Create a QListWidget instance
        list_widget = QListWidget()

        # Add items to the list widget
        for item in items:
            list_widget.addItem(QListWidgetItem(item))

        # Add the list widget to the layout
        layout.addWidget(list_widget)

        # Set the layout of the page
        self.setLayout(layout)
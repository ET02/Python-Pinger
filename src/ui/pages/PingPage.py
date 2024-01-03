from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem

class PingPage(QWidget):
    def __init__(self, name, items):
        super().__init__()
        self.name = name

        # Create a QVBoxLayout instance
        self.layout = QVBoxLayout()

        # Create a QListWidget instance
        self.list_widget = QListWidget()

        # Add items to the list widget
        self.update_items(items)

        # Add the list widget to the layout
        self.layout.addWidget(self.list_widget)

        # Set the layout of the page
        self.setLayout(self.layout)

    def update_items(self, items):
        """Update the list widget with new items."""
        # Clear the list widget
        self.list_widget.clear()

        # Add new items to the list widget
        for item in items:
            self.list_widget.addItem(QListWidgetItem(item))
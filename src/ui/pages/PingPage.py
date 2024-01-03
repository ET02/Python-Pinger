from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QApplication

class PingPage(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name

        # Create a QVBoxLayout instance
        self.layout = QVBoxLayout()

        # Create a QListWidget instance
        self.list_widget = QListWidget()

        # Add the list widget to the layout
        self.layout.addWidget(self.list_widget)

        # Add items to the list widget
        QApplication.instance().data.data_changed.connect(self.update_view)
        self.update_view()

        # Set the layout of the page
        self.setLayout(self.layout)


    def update_view(self):
        # Update the view with the new data
        new_data = QApplication.instance().data.get_array()
        print(new_data)
        # Update the view with new_data...
        self.list_widget.clear()
        for item in new_data:
            list_item = QListWidgetItem(item)
            self.list_widget.addItem(list_item)
        
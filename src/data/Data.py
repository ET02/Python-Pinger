from PyQt6.QtCore import pyqtSignal, QObject

class Data(QObject):
    data_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.array = []

    def add_item(self, item):
        """Add an item to the array."""
        self.array.append(item)
        self.data_changed.emit()

    def remove_item(self, item):
        """Remove an item from the array."""
        if item in self.array:
            self.array.remove(item)
        self.data_changed.emit()

    def get_array(self):
        """Get the array."""
        return self.array
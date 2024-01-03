from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self, on_button_clicked):
        super().__init__()
        self.button = QPushButton("Click me")
        self.button.clicked.connect(on_button_clicked)
        self.setCentralWidget(self.button)
        self.resize(800, 500)

        # find the center of the screen and move the window there
        screen = QApplication.primaryScreen()
        rect = screen.availableGeometry()  # use availableGeometry instead of geometry
        center = rect.center()

        self.move(center.x() - self.width() // 2, center.y() - self.height() // 2)

def start_app(on_button_clicked):
    app = QApplication([])
    window = MainWindow(on_button_clicked)
    window.show()
    app.exec()
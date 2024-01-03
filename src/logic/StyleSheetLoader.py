def load_stylesheet(app, filename):
    
    with open(filename, "r") as file:
        stylesheet = file.read()
        app.setStyleSheet(stylesheet)

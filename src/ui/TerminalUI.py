class TerminalUI:
    def __init__(self):
        """Initialize a new TerminalUI."""
        self.windows = []
        self.commands = {
            'create_window': self.create_window,
            'create_label': self.create_label,
            'exit': self.exit
        }
        self.running = True

    def create_window(self, title, width, height):
        """Create a new window."""
        window = Window(title, width, height)
        self.windows.append(window)
        return window

    def create_label(self, text, x, y):
        """Create a new label."""
        return Label(text, x, y)

    def exit(self):
        """Exit the UI."""
        self.running = False

    def run(self):
        """Run the UI."""
        while self.running:
            command_line = input('Enter command: ')
            command_parts = command_line.split()
            command = command_parts[0]
            args = command_parts[1:]
            if command in self.commands:
                self.commands[command](*args)
            else:
                print(f'Unknown command: {command}')

class Window:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.components = []

    def add(self, component):
        self.components.append(component)

    def display(self):
        print(self.title)
        for component in self.components:
            print(component.text)

class Label:
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

def simple_terminal_ui():
    """Simple terminal UI."""
    # Create a terminal UI
    ui = TerminalUI()

    # Create a window
    window = ui.create_window("Simple Terminal UI", 80, 24)

    # Create a label
    label = ui.create_label("Hello, world!", 1, 1)

    # Add the label to the window
    window.add(label)

    # Run the UI
    ui.run()
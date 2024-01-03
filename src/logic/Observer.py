class Observer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Observer, cls).__new__(cls, *args, **kwargs)
            cls._instance.data = {
                'ping': [],
                'array2': [],
                # Add more variables as needed
            }
            cls._instance.observers = []
        return cls._instance

    def add_observer(self, observer):
        """Add an observer that will be notified when the data changes."""
        self.observers.append(observer)

    def update_data(self, key, new_value):
        """Update the data and notify observers."""
        if key in self.data:
            self.data[key] = new_value
            for observer in self.observers:
                observer.update_items(key, self.data[key])
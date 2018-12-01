class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine_type):
        """Initializes name and type of cuisine attributes."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(self.name + " serves " + self.cuisine_type + ".")
    
    def open_restaurant(self):
        """Print a message that the restaurant is now open."""
        print(self.name + " is now open!")
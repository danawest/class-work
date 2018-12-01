class User():
    """Model a user profile."""
    def __init__(self, first_name, last_name, age, location):
        "Initializes user profile contents."
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
    
    def describe_user(self):
        """Prints a summary of the user's profile."""
        print("User information: " + self.first_name + " " + self.last_name + " is " + str(self.age) + 
              " and lives in " + self.location + ".")
    
    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print("Hello " + self.first_name + "!")
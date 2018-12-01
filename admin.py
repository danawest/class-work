from user import User

class Admin(User):
    """Represent a website administrator."""
    def __init__(self, first_name, last_name, age, location):
        """
        Initialize user profile contents.
        Then initialize attributes specific to Admin.
        """
        super().__init__(first_name, last_name, age, location)
        
        self.privileges = Privileges()

class Privileges():
    """A class to store an administrator's privileges."""
    def __init__(self, privileges=[]):
        self.privileges = privileges
        
    def show_privileges(self):
        """Print a list of Admin privileges."""
        print("\nAs Administrator you have the following privileges: ")
        for privilege in self.privileges:
            print("- " + privilege.title())
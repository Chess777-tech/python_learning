class Restaurant():
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize the restuarant"""
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0
    
    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = f"{self.name} serves wonderful {self.cuisine_type}"
        print(f"\n{msg}")

    def open_resturant(self):
        """Display a message that restaurabt is open"""
        msg = f"{self.name} is now open.. Come on in!! "
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served"""
        self.number_served += number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


class IceCreamStand(Restaurant):
    """Represent an ice cream stand"""
    def __init__(self, name, cuisine_type='ice_cream'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the available flavors"""
        print("\nWe have the following flavors available")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")


big_one = IceCreamStand("Winkie Do's")
big_one.flavors = ['vanilla','chocolate','black cherry']

big_one.describe_restaurant()
big_one.show_flavors()
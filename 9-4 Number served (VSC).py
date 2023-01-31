"""
Add an attribute called number_served with a default value of 0
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who've been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of business.
"""

class Resturant():
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant"""
        self.name = name.title()
        self.cuisine = cuisine_type.title()
        self.number_served = 0

    def describe_resturant(self):
        """Display a summary of the restaurant"""
        msg = f"{self.name} serves wondeful {self.cuisine_type}"
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        msg = f"{self.name} is open. Come on in "
        print(f"\n{msg}")
    
    def set_number_served(self, number_served):
        """Allow the user to set the number of customers that have been served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow the user to increment the number of customers served"""
        self.number_served += additional_served

resturant = Resturant('the mean queen', 'pizza')
resturant.describe_resturant()

print(f"Number served: {resturant.number_served}")
resturant.number_served = 430
print(f"\nNumber served: {resturant.number_served}")

resturant.set_number_served(1257)
print(f"Number served: {resturant.number_served}")

resturant.increment_number_served(239)
print(f"Numbver served: {resturant.number_served}")
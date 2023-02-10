"""
write a loop that prompts the user to enter a series of pizza toppings
until they enter a 'quit' value  
as they enter each topping 
print a message saying you'll add that topping to their pizza 
"""

while True:
    print("\nPlace your order by listing your toppings, when you are finished with your order enter 'quit' to submit your pizza")
    print("------------------------------------------------------------------------------------------------------------------")
    pizza_toppings = input("\nWhat toppings would you like on your pizza: ")

    print(f"{pizza_toppings} has been added to your pizza")

    if pizza_toppings == 'quit':
        print("Your order will be right up. Thank you for your order")
        break

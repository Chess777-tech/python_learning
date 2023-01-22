"""
write a program that polls users about their dream vacation
write a prompt similar to if you could visit one place in the world, where would you go?
include a block of code that prints the results of the poll
"""

responses = dict()
counter = 0 
polling_active = True

while polling_active:
    #Prompt for the person's name and response 
    name = input("\nWhat is your name? ")
    location = input(f"Hello {name}, if you could visit one place in the world, where would you go? ")
    counter += 1
    if location in responses.keys():  #check if location is already been entered
        responses[location] += 1  # if location exists increment it by 1
    else: 
        responses[location] = 1  # if location doesnt exist create the key and assign it to 1
                

    repeat = input("Would you like someone else to respond to the poll? (yes/no) ")
    if repeat == 'no':
        polling_active = False

    
print("\n--- Poll Results---")
for key in responses.keys():
    print(int(f"{responses[key] / counter * 100}% of people in the poll chose {key}"))
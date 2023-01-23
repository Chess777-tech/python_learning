"""
write a in which you ask the user for thier age
then tell them the cost of their movie ticket
AGE:
3 = free
3-12 = $10
12 and older = $15
"""


print("Welcome to Cinemark Movie Theater")
print("-----------------------")
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished purchasing your tickets: "

while True: 
    age =input(prompt)
    if age == 'quit':
        print("Thank you come again")
        break
    age = int(age)

    if age < 3:
        print("Your ticket is Free.")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15. ")
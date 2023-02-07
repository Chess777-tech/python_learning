# Column: name, day/month, celebrates, age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

#problem 1: Celebrations
#loop through all the people in birthdays 
#if they celebrate their birthday, print out 
# "Happy Birthday and their name "

print("Celebrations")

#Solution 1 here 
for entry in BIRTHDAYS:
    name, bday, celebrate, age = entry
    if celebrate:
        print("Happy Birthday {}".format(name))

print("_"*20)

#problem 2: Half birthdays 
#loop through all the people in birthdays 
#calculate their half birthday (six months away )
#print out their name and half birthday 

print("Half Birthdays: ")

#solution 2 here 
for entry in BIRTHDAYS:
    name, bday, celebrate, age = entry
    day, month = bday.split("/")

    if int(month) in range(1,7) or int(month) in range(9,13):
        print("{}".format(name))

print("_"*20)


#Problem 4: Wishing stars
#loop through all the people in birthdays
#if the person celebrates their bday and 
#the pertson is < 10 years old 
#print out their name and the number of stars equivelant to their age 


#solution 4 here
for entry in BIRTHDAYS:
    name, bday, celebrate, age = entry

    stars = ['*' for _ in range(age)]

    if celebrate and age <= 10: 
        print("{} - {}".format(name, ''.join(stars)))

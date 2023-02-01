name = input("Type your Warriors name: ")
print("--------------------------------")
print(f"Welcome {name} to an magical adventure ")

question1 =  input("You're folloing a dirt road and it is coming to an end. You can go right or left? ").lower()
if question1 == "left":
    question2 = input("you come to a river that is blocking your path.. Do you want to cross the river or go around: ").lower()
    
    if question2 == "cross":
        print("You swam across and got killed by a river montster... You Lost")
    elif question2 == "go around":
        print("You have went around the river and proceeded down the path")
    else:   
        print("You lose... invalid answer")

elif question1 == "right":
    question3 = input("You have made your way to an abandon church... Do you want to (explore/turnaround): ")

    if question3 == "back":
        print("You go back and get attackted by a horde of zombies")
    elif question3 == "explore":
        question3 = input("You have found a hidden cave in the basement...do you want to explore the cave or leave the church (explore/leave): ")
    
    if question3 == "explore":
        print("You have found the hidden treasure... You win!!")
    elif question3 == "leave":
        print("The zombies were waiting for you and ate you whole... You lose!!!")
    else:
        print("Not valid option.. You lose")

print("Thank you for playing")



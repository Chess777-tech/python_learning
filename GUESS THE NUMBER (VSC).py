"""
        create a random number 
        ask a user to guess a number (1,x)
        keep track of tries 
        give them 3 tries 
        if answered correctly 
        print aye you gussed correctly 

        if max tries reached give answer answer 
        print(tries ran out, play again!1)
"""



import random

random_number = random.randint(1,100)
guess = 0 


attempts = 0
max_tries = 5  
print("Welcome to my guessing game.")

print(f"You only get {max_tries} tries" )
guess_list = []

while attempts < max_tries:
    guess = int(input(f"Please guess a number between 1 and 100: "))
    if guess in guess_list:
        print("You already guessed " + str(guess))
        continue
    attempts += 1
    guess_list.append(guess)
    if guess > random_number:
        print("Guess was too high. Try again!! ")
    elif guess < random_number:
        print("Guess was too low. Try again!! ")
    elif guess == random_number:
        print("CORRECT ANSWER...YOU WIN", + str(attempts),"guesses")
    elif guess != int(input(guess)):
        print("Enter a integer..Try again")
        break
if attempts >= max_tries:
    print(f"Ran out of tries: {attempts}. The answer was {random_number}.")
 

# Turle Game using the package 'turtle'!

# Import relevant modules
import turtle
import random
import time

# Setting up a nice sceen for our game 
screen = turtle.Screen()
screen.bgcolor('lightblue')  # Background color 

# We want two players in this game 
# The ideas is whoever crosses finish line wins 

# Player One - Basic set up
player_one = turtle.Turtle()
# Color of player one 
player_one.color('blue')
# Make this player a turtle
player_one.shape('turtle')

# PLayer Two - basic set up
player_two = player_one.clone()
# Color of player two
player_two.color('red')

# Lets position our players!
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)

# Now lets draw a finish line 
player_one.goto(300,-250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('    Finish!!',font=24 )

# Allows player one to return to start position 
player_one.penup()
player_one.color('blue')
player_one.goto(-300,200)
player_one.right(90)

# We need to make sure both players have their pen down
player_one.pendown()
player_two.pendown()

# Lets create values for the die 
die = [1,2,3,4,5,6]

# Lets create the Game :)

for i in range(30):
    if player_one.pos() >= (300,250):
        print("Player One: Won the race!!!")
        break
    elif player_two.pos() >= (300,-250):
        print("Player Two: Won the race!!!")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30*die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30*die_roll)
        time.sleep(1)




# This keeps the turtle drawing on the screen
#turtle.done()
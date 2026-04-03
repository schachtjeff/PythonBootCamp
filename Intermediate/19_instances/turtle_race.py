# Imports
from turtle import Turtle, Screen
import random

#Globals
is_race_on = False
finish_line_coord = 230
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_start = 175

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)

# User window to make a selection
user_choice = screen.textinput(title="Make your choice", prompt="Which turtle will win the race? Enter a color: ")
print(user_choice)

# Setup the turtles for race
for color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    y_start -= 50
    new_turtle.goto(x=-230, y=y_start)
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

# Start the race
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > finish_line_coord:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry :( The {winning_color} turtle is the winner!  Try again!")
        rand_distance = random.randint(0, 10)
        turtle.forward((rand_distance))


screen.exitonclick()

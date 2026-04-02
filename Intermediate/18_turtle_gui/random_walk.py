# Wikipedia: https://en.wikipedia.org/wiki/Random_walk
from turtle import Turtle, Screen
import random

# Init object, then give drawing pen size and speed
arrow = Turtle()
arrow.pensize(15)
arrow.speed("fastest")

# Globals
colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
directions = [0, 90, 180, 270]
moving_forward = 30
number_of_movements = 200

for i in range(number_of_movements):
    arrow.color(random.choice(colors))
    arrow.forward(moving_forward)
    arrow.setheading(random.choice(directions))



# Keep the window present
screen = Screen()
screen.exitonclick()
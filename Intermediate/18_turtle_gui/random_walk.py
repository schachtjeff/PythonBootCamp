# Wikipedia: https://en.wikipedia.org/wiki/Random_walk
import turtle as t
from turtle import Turtle, Screen
import random

# Init object, then give drawing pen size and speed
arrow = Turtle()
t.colormode(255)
arrow.pensize(15)
arrow.speed("fastest")

# Globals
#colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
directions = [0, 90, 180, 270]
moving_forward = 30
number_of_movements = 200

def random_color() -> tuple[int, int, int]:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

for i in range(number_of_movements):
    arrow.pencolor(random_color())
    arrow.forward(moving_forward)
    arrow.setheading(random.choice(directions))

# Keep the window present
screen = Screen()
screen.exitonclick()
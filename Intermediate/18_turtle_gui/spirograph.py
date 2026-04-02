# Draw a spirograph
import turtle as t
from turtle import Turtle, Screen
import random

# Init object, then give drawing pen size and speed
arrow = Turtle()
t.colormode(255)
arrow.speed("fastest")

#Globals
circle_radius = 100
shift_heading = 10
number_of_circles = 100
degrees_in_circle = 360
gap_size = 5


def random_color() -> tuple[int, int, int]:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_spirograph(size_of_gap):
    for i in range(int(degrees_in_circle / size_of_gap)):
        arrow.color(random_color())
        arrow.circle(radius=circle_radius)
        #setheading needs int
        arrow.setheading(arrow.heading() + size_of_gap)

draw_spirograph(size_of_gap=gap_size)


# Keep the window present
screen = Screen()
screen.exitonclick()
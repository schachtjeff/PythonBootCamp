# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, and nanagon
# Also give it different colors
from turtle import Turtle, Screen

# Init object, then give shape and color
arrow = Turtle()

# Globals
draw_line = 100
starting_sides = 3
number_of_shapes = 6
degrees_of_turning = 360
colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
color_option = 0

# Initial loop
for i in range(number_of_shapes):
    degrees_of_shape = degrees_of_turning / starting_sides
    for side in range(starting_sides):
        arrow.color(colors[color_option])
        arrow.right(degrees_of_shape)
        arrow.forward(draw_line)
    starting_sides += 1
    draw_line += 10
    color_option += 1

# Keep the window present
screen = Screen()
screen.exitonclick()
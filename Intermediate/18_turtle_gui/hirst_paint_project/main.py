import colorgram
import turtle as t
import random
from turtle import Screen

#Globals
rgb_colors = []
t.colormode(255)
dot_size = 20
move_forward = 50
number_of_dots = 100
init_heading = 0
adjust_heading = 225
init_forward = 250
turn_left = 90
turn_backwards = 180
back_to_start_pos = 500
dot_row = 10

#Extract the colors from the image
print("Extracting colors")
colors = colorgram.extract(f='hirst_image.jpg', number_of_colors=30)
# get the colors into a list of tuples
print("listing colors")
for color in colors:
    #rgb_colors.append(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

painter = t.Turtle()
painter.speed("fastest")
painter.penup()
painter.hideturtle()

# get the painter into the starting position
painter.setheading(adjust_heading)
painter.forward(init_forward)
painter.setheading(init_heading)

print("Painting colors")
for num_dots in range(1, number_of_dots + 1):
    painter.dot(dot_size, random.choice(rgb_colors))
    painter.forward(move_forward)

    if num_dots % dot_row == 0:
        painter.setheading(turn_left)
        painter.forward(move_forward)
        painter.setheading(turn_backwards)
        painter.forward(back_to_start_pos)
        painter.setheading(init_heading)

print("All done!")
# Keep the window present
screen = Screen()
screen.exitonclick()
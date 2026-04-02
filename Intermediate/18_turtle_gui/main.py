# Turtle graphics library
#https://docs.python.org/3/library/turtle.html

from turtle import Turtle, Screen

# Init object, then give shape and color
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# Colors -> https://trinket.io/docs/colors  - CSS name
timmy_the_turtle.color("DeepSkyBlue")

# move the turtle
timmy_the_turtle.forward(100)

# Keep the window present
screen = Screen()
screen.exitonclick()
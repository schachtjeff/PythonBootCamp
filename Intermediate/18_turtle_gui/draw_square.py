from turtle import Turtle, Screen

# Init object, then give shape and color
arrow = Turtle()

# move the turtle into a square
for i in range(4):
    arrow.forward(100)
    arrow.right(90)


# Keep the window present
screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen

# Init object, then give shape and color
arrow = Turtle()

number_of_drawn_lines = 20
equal_forward_movement = 10

# move arrow with dashed lines
for i in range(number_of_drawn_lines):
    arrow.forward(equal_forward_movement)
    # essentially the drawn line of the pen is up
    arrow.penup()
    arrow.forward(equal_forward_movement)
    # essentially puts the drawing pen back down
    arrow.pendown()


# Keep the window present
screen = Screen()
screen.exitonclick()
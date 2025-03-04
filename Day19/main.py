from turtle import Turtle, Screen
# Higher Order Functions

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
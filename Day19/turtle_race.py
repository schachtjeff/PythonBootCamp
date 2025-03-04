import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your choice", prompt="Which turtle will win the race? Enter a color: ")
print(user_choice)
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
finish_line_coord = 230

y_start = 175
for color in turtle_colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    y_start -= 50
    new_turtle.goto(x=-230, y=y_start)
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > finish_line_coord:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry :(  You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward((rand_distance))


screen.exitonclick()

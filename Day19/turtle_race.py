from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your choice", prompt="Which turtle will win the race? Enter a color: ")
print(user_choice)
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_start = 175
for color in turtle_colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    y_start -= 50
    tim.goto(x=-230, y=y_start)

screen.exitonclick()

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("A Snake Game")
snake_color = "white"
all_snake = []
snake_start = 1
x_start = -30

while snake_start <= 3:
    snake_start += 1
    new_link = Turtle(shape="square")
    new_link.color(snake_color)
    new_link.penup()
    new_link.goto(x=x_start, y=0)
    x_start += 20
    all_snake.append(new_link)









screen.exitonclick()

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("A Snake Game")
# gives delay between segments so it looks like a line
screen.tracer(0)
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

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for seg_num in range(len(all_snake) - 1, 0, -1):
        new_x = all_snake[seg_num - 1].xcor()
        new_y = all_snake[seg_num - 1].ycor()
        all_snake[seg_num].goto(new_x, new_y)
    all_snake[0].forward(20)



screen.exitonclick()

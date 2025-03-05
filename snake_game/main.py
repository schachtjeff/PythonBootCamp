from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WALLS = 280
NEG_WALLS = -280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("A Snake Game")
# gives delay between segments so it looks like a line
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detect collision of food with snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with the wall
    if snake.head.xcor() > WALLS \
            or snake.head.xcor() < NEG_WALLS \
            or snake.head.ycor() > WALLS \
            or snake.head.ycor() < NEG_WALLS:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

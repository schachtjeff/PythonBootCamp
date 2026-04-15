#Imports
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initiate screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Create the turtle to cross
start_level_pos = (0, -275)
timmy = Player(start_level_pos)

# Listen for up arrow key to move the player
screen.listen()
screen.onkey(timmy.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# Exit the game when done.
screen.exitonclick()

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
timmy = Player()
car_manager = CarManager()

# Listen for up arrow key to move the player
screen.listen()
screen.onkey(timmy.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_new_car()
    car_manager.move_cars()


    # Detect the collision of timmy with the cars
    for car in car_manager.all_moving_cars:
        if car.distance(timmy) < 20:
            game_is_on = False

    # Detect the finish line and do actions
    if timmy.is_at_finish_line():
        car_manager.increase_speed()
        timmy.reset_position()

    # manage memory, maybe
    car_manager.destroy_cars()

# Exit the game when done.
screen.exitonclick()

#Imports
import random
from turtle import Turtle

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X_POS = 300
RANDOM_Y_POS_LOWER = -250
RANDOM_Y_POS_UPPER = 250


class CarManager:
    def __init__(self):
        self.all_moving_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_new_car(self) -> None:
        if self.is_create_new_car():
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y_pos = random.randint(RANDOM_Y_POS_LOWER, RANDOM_Y_POS_UPPER)
            new_car.goto(START_X_POS, random_y_pos)
            self.all_moving_cars.append(new_car)

    def move_cars(self) -> None:
        for car in self.all_moving_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def is_create_new_car(self) -> bool:
        #Random chance every 1 and 6 chances
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            return True
        else:
            return False

    def destroy_cars(self):
        for car in self.all_moving_cars:
            if car.xcor() < -350:
                self.all_moving_cars.remove(car)

    def increase_speed(self) -> None:
        self.car_speed += MOVE_INCREMENT



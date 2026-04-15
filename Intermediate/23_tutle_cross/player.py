#Imports
from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, xy_coordinate):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.right(angle=270)
        self.goto(xy_coordinate)

    def go_up(self) -> None:
        new_y_cord = self.ycor() + 20
        self.goto(self.xcor(), new_y_cord)

    def reset_position(self, xy_coordinate):
        self.goto(xy_coordinate)

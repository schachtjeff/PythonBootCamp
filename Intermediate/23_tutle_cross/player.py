#Imports
from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(to_angle=90)
        self.goto(STARTING_POSITION)

    def go_up(self) -> None:
        new_y_cord = self.ycor() + 20
        self.goto(self.xcor(), new_y_cord)

    def reset_position(self) -> None:
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

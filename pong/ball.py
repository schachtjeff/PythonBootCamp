from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = self.get_random_x()
        self.y_move = 10 
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def get_random_x(self):
        return randint(3, 20)
    
    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        x = self.get_random_x()
        if self.x_move < 0:
            x *= -1
        self.x_move = x * -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_bounce()
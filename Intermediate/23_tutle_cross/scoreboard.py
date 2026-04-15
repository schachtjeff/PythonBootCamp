#Imports
from turtle import Turtle

# constants
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 200)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(-250, 200)
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def level_up(self) -> None:
        self.level += 1

    def game_over_message(self) -> None:
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

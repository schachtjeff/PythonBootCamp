# Imports
from turtle import Turtle

# Constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # No longer running game over, going to reset the score
    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self) -> None:
        self.score += 1
        # clear is so score doesn't overlap previous scores
        #self.clear()
        self.update_scoreboard()

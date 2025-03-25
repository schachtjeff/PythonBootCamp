from turtle import Turtle

GAME_WINNER = 5


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        self.l_score += 1

    def right_point(self):
        self.r_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def get_winner(self):
        if self.l_score == GAME_WINNER:
            print("left paddle won!")
            return True
        elif self.r_score == GAME_WINNER:
            print("right paddle won!")
            return True
        else:
            return False        

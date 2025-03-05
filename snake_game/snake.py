from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self._snake_color = "white"
        self.x_start = -30
        self.create_snake()


    def create_snake(self) -> None:
        start_links = 1
        while start_links <= 3:
            start_links += 1
            new_link = Turtle(shape="square")
            new_link.color(self._snake_color)
            new_link.penup()
            new_link.goto(x=self.x_start, y=0)
            self.x_start += 20
            self.segments.append(new_link)

    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

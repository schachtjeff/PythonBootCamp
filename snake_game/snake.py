from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self._snake_color = "white"
        self.x_start = -30
        self.create_snake()
        self.head = self.segments[0]


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
        self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


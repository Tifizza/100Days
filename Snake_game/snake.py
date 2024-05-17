from turtle import Turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]
        self.tail = self.blocks[-1]

    def create_snake(self):
        for i in range(3):
            self.blocks.append(Turtle("square"))
            self.blocks[i].color("white")
            self.blocks[i].penup()
            self.blocks[i].goto(0 - i * 20, 0)

    def move(self):
        for i in range(len(self.blocks) - 1, 0, -1):
            self.blocks[i].goto(self.blocks[i - 1].xcor(), self.blocks[i - 1].ycor())
        self.blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def eating(self):
        self.blocks.append(Turtle("square"))
        self.blocks[len(self.blocks)-1].color("white")
        self.blocks[len(self.blocks)-1].penup()
        self.blocks[len(self.blocks) - 1].goto(self.tail.xcor(), self.tail.ycor())

    def check_body_collision(self):
        for block in self.blocks[1:]:
            if block.distance(self.head) < 15:
                return True


from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_over()
        self.left(90)
        self.hideturtle()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def start_over(self):
        self.goto(STARTING_POSITION)

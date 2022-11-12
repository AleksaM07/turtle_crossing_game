from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.reset()

    def level_up(self):
        self.level += 1
        self.write(f"Level {self.level}", align="left", font=FONT)

    def reset(self):
        self.clear()
        self.setposition(-260, 260)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align="center", font=FONT)


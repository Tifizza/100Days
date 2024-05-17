from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = -1
        self.goto(0, 270)
        self.color("White")
        self.refresh_score()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over !", align='center', font=('Courier', 30, 'normal'))


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("White")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "bold"))

    def add(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("White")
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))





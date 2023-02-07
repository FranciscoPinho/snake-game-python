from turtle import Turtle
import os

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font=('Arial', 14, 'normal'))

    def increment(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()

    def set_high_score_from_file(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt") as file:
                contents = int(file.read())
                self.high_score = contents
                self.write_score()


    # def game_over(self):
    #   self.goto(0, 0)
    #  self.write("GAME OVER", False, align="center", font=('Arial', 14, 'normal'))

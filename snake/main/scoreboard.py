from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"Score: {self.score} High score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def reset(self):

       if self.score> self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def gameover(self):
        self.goto(-150,0)
        self.write("GAME OVER",font=("Courier", 50, "normal"))





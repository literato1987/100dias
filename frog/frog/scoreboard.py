from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.color("black")
        self.penup()
        self.goto(-200, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 265)
        self.write(f"LEVEL:{self.level}", align="center", font=FONT)



    def level_up(self):
        self.level+=1
        self.update_scoreboard()

    def gameover(self):
        self.goto(-150, 0)
        self.write("GAME OVER",font=("Courier", 50, "normal"))


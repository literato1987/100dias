from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("green")
        self.shape("turtle")
        self.seth(90)
        self.goto(STARTING_POSITION)


    def go_up(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
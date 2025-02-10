from turtle import Turtle
class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pu()
        self.color("white")
        self.shape("circle")
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1  # Corrected: x direction
        self.move_speed*=1.1

    def bounce_y(self):
        self.y_move *= -1  # Corrected: y direction

    def reset_position(self):
        self.goto(0, 0)

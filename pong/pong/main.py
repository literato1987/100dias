from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball((0,0))
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()
    #detect collision with paddle
    if (ball.xcor() > 320 and ball.distance(r_paddle)<50) or (ball.xcor() < -320 and ball.distance(l_paddle)<50):
        ball.bounce_x()
    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect R paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()




screen.exitonclick()

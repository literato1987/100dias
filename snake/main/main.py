from turtle import Screen, Turtle

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake=Snake()
food=Food()
screen.listen()
scoreboard=Scoreboard()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(1 / 10)
    snake.move()

    if snake.head.distance(food)<10:
        print("ñam ñam")
        food.move()
        scoreboard.increase_score()
        print(scoreboard.score)
        snake.grow()
    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()





screen.exitonclick()
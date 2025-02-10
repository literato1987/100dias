import time
from turtle import Screen
from player import Frog, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

frog=Frog()
scoreboard=Scoreboard()
car_manager=CarManager()


screen.listen()
screen.onkeypress(frog.go_up,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()


    if frog.ycor()>FINISH_LINE_Y:
        frog.reset_position()
        scoreboard.level_up()
        car_manager.accelerate()
    #
    for car in car_manager.all_cars:
        if car.distance(frog)<20:
            scoreboard.gameover()
            game_is_on = False



screen.exitonclick()
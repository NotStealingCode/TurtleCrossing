import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

next_stage_reached = 280
crashed = 24
game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    car_manager.generate_cars()
    car_manager.move_cars()
    if player.ycor() >= next_stage_reached:
        player.next_stage()
        scoreboard.increase_level()
        car_manager.increase_speed()

    for check in car_manager.cars:
        if player.distance(check) < crashed:
            car_manager.stop_cars()
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()

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
screen.onkey(fun=player.move,key="Up")

game_loop = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if game_loop == 6:
        car_manager.create_car()
        game_loop = 0
    car_manager.move_car()
    if player.ycor() == 280:
        player.win()
        scoreboard.increase_level()
        car_manager.level_up()
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            # print("Game Over")
            scoreboard.game_over()
            game_is_on = False
    game_loop += 1


screen.exitonclick()
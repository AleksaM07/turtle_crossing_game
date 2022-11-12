import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random as r
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing game")
cars = []

player = Player()
scorebored = Scoreboard()

screen.onkeypress(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    spam_procent = r.uniform(0.0, 1.0)

    if spam_procent > 0.6:
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.move_car(STARTING_MOVE_DISTANCE)

    #delaying turtle start
    if len(cars) > 25:
        screen.listen()
        player.showturtle()

    #Turtle goes to the end of the screen / levels up
    if player.ycor() > FINISH_LINE_Y:
        player.start_over()
        scorebored.level_up()
        scorebored.reset()
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    #deceting collision with the cars
    for car in cars:
        if player.distance(car) < 25:
            scorebored.game_over()
            game_is_on = False

screen.exitonclick()

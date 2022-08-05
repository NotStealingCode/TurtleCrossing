from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STOP_MOVE = 0
LEFT = 180
DEFAULT_X = 300


class CarManager:
    def __init__(self):
        self.cars = []
        self.starting_move_distance = 5

    def generate_cars(self):
        random_number = random.randint(1, 5)
        if random_number == 3:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(DEFAULT_X, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for cars in self.cars:
            cars.setheading(LEFT)
            cars.forward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT
        for increase_speed in self.cars:
            increase_speed.forward(self.starting_move_distance)

    def stop_cars(self):
        for stop in self.cars:
            stop.forward(STOP_MOVE)

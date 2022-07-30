from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colors = ["royal blue", "green", "yellow", "red", "deep pink", "light coral", "orange red", "dark slate blue"]

sides = [3, 4, 5, 6, 7, 8, 9, 10]

for _ in sides:
    tim.color(random.choice(colors))
    for num_sides in range(_):
        tim.forward(80)
        tim.right(360/_)
        



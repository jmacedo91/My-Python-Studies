from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

colors = ["royal blue", "green", "yellow", "red", "deep pink", "light coral", "orange red", "dark slate blue"]
angles = [0, 90, 180, 270]
tim.pensize(10)
tim.speed("fastest")


for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(random.randint(1, 50))
    tim.setheading(random.choice(angles))

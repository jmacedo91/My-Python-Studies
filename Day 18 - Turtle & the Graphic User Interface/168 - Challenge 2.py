from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.color("green")
tim.penup()

def dashed_line():
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

for _ in range(10):
    dashed_line()

screen = Screen()
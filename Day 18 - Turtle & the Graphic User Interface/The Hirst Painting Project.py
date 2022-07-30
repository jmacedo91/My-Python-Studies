import colorgram
import turtle as t
import random


def color_palette(image, num_of_colors):
    colors = colorgram.extract(image, num_of_colors)
    rgb = list()

    for color in colors:
        color = (color.rgb.r, color.rgb.g, color.rgb.b)
        rgb.append(color)

    return rgb


#TODO: Creating the color palette
hirst_colors = color_palette("Ellipticine.jpg", 20)
t.colormode(255)

#TODO: Creating my pencil
pencil = t.Turtle()
pencil.shape("circle")
pencil.pensize(20)
pencil.speed("fastest")

#TODO: Setting the initial position
pencil.penup()
pencil.goto(-320, -320)
pencil.hideturtle()

#TODO: Painting the picture
for row in range(10):
    for column in range(10):
        dot_color = random.choice(hirst_colors)
        pencil.pencolor(dot_color)
        pencil.pendown()
        pencil.forward(0)
        pencil.penup()
        pencil.forward(70)
    pencil.backward(700)
    pencil.left(90)
    pencil.penup()
    pencil.forward(70)
    pencil.right(90)

screen = t.Screen()
screen.exitonclick()
screen.screensize(900, 900)

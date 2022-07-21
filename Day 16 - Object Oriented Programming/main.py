# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# # TODO Building the object
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkGreen")
# i = 0
#
# # TODO Drawning a square.
# while i < 4:
#     timmy.forward(100)
#     timmy.left(90)
#     i += 1
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align)

table.align = "l"
print(table)
print(table.align)

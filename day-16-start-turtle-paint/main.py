# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("DarkOrange")
# timmy.forward(100)
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import  PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
#print(table.align)
table.align["Pokemon Name"] = "l"
table.add_column("Pokemon Type", ["electric", "fire", "water"])
print(table)
#print(table.align)


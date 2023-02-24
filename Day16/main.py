#Coffee Machine OOPS!

# from turtle import Turtle, Screen

# tom = Turtle()
# print(tom.shape("turtle"))
# print(tom.color("darkslategrey"))
# print(tom.forward(100))
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
from prettytable import PrettyTable
x = PrettyTable()
x.add_column("Pokemon Name",["Pikachu", "Squirtle", "Bulbasaur", "Charmander"])
x.add_column("Pokemon Type",["electric", "water", "grass", "Fire"])
x.align = 'l'
print(x)

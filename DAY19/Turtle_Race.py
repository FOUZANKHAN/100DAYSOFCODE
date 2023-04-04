from turtle import Turtle, Screen
import random
is_game_on = False
screen =  Screen()
#width, height
screen.setup(500, 400)
user_bet = screen.textinput(title = "Make your bet ", prompt = "Which turtle will win the race? Enter Color: ")
colors = ["violet", "Blue", "Green", "Yellow", "Orange", "Red"]
ypos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = ypos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_game_on = False
            if winning_color == user_bet:
                print(f"You're turtle won, {winning_color}")
            else:
                print(f"You lose, the winner is {winning_color} turtle")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
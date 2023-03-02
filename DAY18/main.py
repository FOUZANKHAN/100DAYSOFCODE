from turtle import Screen
import turtle as t

tim = t.Turtle()
t.colormode(255)
tim.shape('turtle')
tim.color("dim gray")

# for _ in range(4):
#     tim.fd(100)
#     tim.right(90)
#     tim.fd(100)
# for _ in range(50):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()
import random
# def draw_shape(num_sides):
#     colors = ["cyan", "red", "black", "white smoke", "blue", "aquamarine", "SeaGreen"]
#     tim.color(random.choice(colors))
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         tim.fd(100)
#         tim.right(angle)
# f = 3
# while f <=10:
#     draw_shape(f)
#     f += 1
def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    randomcol = (r,g,b)
    return randomcol
# def randomwalk():
#     angles = [0, 90, 180, 270]
#     for _ in range(80):
#         colors = randomcolor()
#         tim.pensize(5)
#         tim.color(colors)
#         tim.fd(20)
#         tim.seth(random.choice(angles))
#         tim.speed("fastest")

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(randomcolor())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spirograph(5)
#randomwalk()





screen = Screen()
screen.exitonclick()
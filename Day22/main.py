from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.title("PONG GAME FROM F")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up" )
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.paddle_bounce()


    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.lpoint()
        scoreboard.update_scoreboard()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint()
        scoreboard.update_scoreboard()






screen.exitonclick()
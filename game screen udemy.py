from turtle import Screen, Turtle
from Pad_1 import Paddle1
from Pad_2 import Paddle2
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle1_on = Paddle1((350, 0))
paddle2_on = Paddle2((-350, 0))
ball_on = Ball()


screen.listen()
screen.onkey(paddle1_on.move_up, key='Up')
screen.onkey(paddle1_on.move_down, key='Down')
screen.onkey(paddle2_on.move_up, key='w')
screen.onkey(paddle2_on.move_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball_on.move_ball_udemy()

    if ball_on.ycor() > 280 or ball_on.ycor() < -280:
        ball_on.bounce_udemy()

screen.exitonclick()


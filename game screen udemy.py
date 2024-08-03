from turtle import Screen, Turtle
from Pad_1 import Paddle1
from Pad_2 import Paddle2
from ball import Ball
import time
from scoreboard import Scoreboard


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


def game_loop(start_side):

    if ball_on.xcor() > 340 or ball_on.xcor() < -340:  # out of bands detection
        print(f'game over{ball_on.xcor()}')
        ball_on.game_over()  # ball position reset
        game_loop(ball_on.xcor())
        while game_is_on:
            time.sleep(0.1)
            screen.update()
            if start_side < 0:
                ball_on.move_ball_1_udemy()
            elif start_side > 0:
                ball_on.move_ball_2_udemy()

            game_loop(ball_on.xcor())

    if ball_on.ycor() > 280 or ball_on.ycor() < -280:
        ball_on.bounce_y_udemy()

    # Detect collision with r_paddle
    if ball_on.distance(paddle1_on) < 50 and ball_on.xcor() > 320 or ball_on.distance(
            paddle2_on) < 50 and ball_on.xcor() < -320:
        ball_on.bounce_x()


def game_start(start_side=-1):
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        ball_on.move_ball_1_udemy()
        # game_loop(ball_on.xcor())
        if ball_on.ycor() > 280 or ball_on.ycor() < -280:
            ball_on.bounce_y_udemy()

        if ball_on.distance(paddle1_on) < 50 and ball_on.xcor() > 320 or ball_on.distance(
                paddle2_on) < 50 and ball_on.xcor() < -320:
            ball_on.bounce_x()

        if ball_on.xcor() > 380:
            ball_on.reset()

        if ball_on.xcor() < -380:
            ball_on.reset()


score = Scoreboard()

sleep = 0.1
# game_start()
while game_is_on:
    time.sleep(sleep)
    screen.update()
    ball_on.move_ball_1_udemy()
    # game_loop(ball_on.xcor())

    if ball_on.ycor() > 280 or ball_on.ycor() < -280:
        ball_on.bounce_y_udemy()

    if ball_on.distance(paddle1_on) < 50 and ball_on.xcor() > 320 or ball_on.distance(
            paddle2_on) < 50 and ball_on.xcor() < -320:
        sleep -= 0.01
        ball_on.bounce_x()

    if ball_on.xcor() > 380:
        score.r_point()
        ball_on.game_over()

    if ball_on.xcor() < -380:
        ball_on.game_over()
        score.l_point()
screen.exitonclick()


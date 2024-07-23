from turtle import Screen, Turtle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("green")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def move_up():
    # Paddle.setheading(90)
    y_up_cor = paddle.ycor() + 10
    paddle.goto(x=350, y=y_up_cor)
    return


def move_down():
    # Paddle.setheading(90)
    y_down_cor = paddle.ycor() - 10
    paddle.goto(x=350, y=y_down_cor)
    return


screen.listen()
screen.onkey(move_up, key='Up')
screen.onkey(move_down, key='Down')


game_on = True
while game_on:
    screen.update()

screen.exitonclick()
from turtle import Screen, Turtle




# screen.tracer(0, 0)


# screen.update()


class PongGame:

    def __init__(self):
        self.screen = Screen()
        self.paddle = Turtle()

        pass

    def paddle_on(self):
        self.paddle.shape('square')
        self.paddle.penup()
        self.paddle.color('Green')
        self.paddle.shapesize(5, 1)
        self.paddle.goto(x=350, y=0)

    def game_on(self):
        self.screen.tracer(0)
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Pong')
        self.paddle_on()
        self.screen.tracer(1)
        self.screen.listen()
        self.screen.onkey(self.move_up, key='Up')
        self.screen.onkey(self.move_down, key='Down')
        self.screen.exitonclick()

    def move_up(self):
        # Paddle.setheading(90)
        up_cor = self.paddle.ycor() + 10
        self.paddle.goto(x=350, y=up_cor)
        return self

    def move_down(self):
        # Paddle.setheading(90)
        down_cor = self.paddle.ycor() - 10
        self.paddle.goto(x=350, y=down_cor)
        return self


game = PongGame()
game.game_on()




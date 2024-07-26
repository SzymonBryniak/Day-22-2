from turtle import Screen, Turtle
from Pad_1 import Paddle1
from Pad_2 import Paddle2
from ball import Ball


class PongGame:

    def __init__(self):
        self.screen = Screen()
        # self.screen.tracer(0)
        self.paddle1_on = Paddle1((350, 0))
        self.paddle2_on = Paddle2((-350, 0))
        self.ball_on = Ball((0, 0))

    def game_on(self):
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Pong')
        game_on = True
        self.ball_on.goto(260, 40)
        self.screen.listen()
        self.screen.onkey(self.paddle1_on.move_up, key='Up')
        self.screen.onkey(self.paddle1_on.move_down, key='Down')
        self.screen.onkey(self.paddle2_on.move_up, key='w')
        self.screen.onkey(self.paddle2_on.move_down, key='s')
        self.screen.exitonclick()
        while game_on:
            self.screen.update()
        print(1)


game = PongGame()
game.game_on()

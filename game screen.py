from turtle import Screen, Turtle
from Pad_1 import Paddle1
from Pad_2 import Paddle2
from ball import Ball
import time


class PongGame:

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Pong')
        self.ball_on = Ball((0, 0))
        self.paddle1_on = Paddle1((350, 0))
        self.paddle2_on = Paddle2((-350, 0))
        self.game_is_on = True
        self.screen.listen()
        self.screen.onkey(self.paddle1_on.move_up, key='Up')
        self.screen.onkey(self.paddle1_on.move_down, key='Down')
        self.screen.onkey(self.paddle2_on.move_up, key='w')
        self.screen.onkey(self.paddle2_on.move_down, key='s')
        self.game_on()
        self.screen.exitonclick()
        # while self.game_is_on:
        #     self.ball_on.move_ball()
        #     time.sleep(1)
        #     self.screen.update()

    def game_on(self):
        # self.screen.tracer(0)
        # self.screen.tracer(0)
        game_is_on = True
        while game_is_on:
            self.screen.tracer(0)
            self.ball_on.setpos(0, 0)
            self.screen.update()
            self.screen.tracer(1)
            self.ball_on.move_ball()
            


game = PongGame()
# game.game_on()

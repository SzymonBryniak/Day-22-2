from turtle import Screen, Turtle
from Pad_1 import Paddle1
from Pad_2 import Paddle2


class PongGame:

    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.paddle1_on = Paddle1((350, 0))
        self.paddle2_on = Paddle2((-350, 0))

    def game_on(self):
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor('black')
        self.screen.title('Pong')
        self.screen.listen()
        self.screen.onkey(self.paddle1_on.move_up, key='Up')
        self.screen.onkey(self.paddle1_on.move_down, key='Down')
        self.screen.onkey(self.paddle2_on.move_up, key='w')
        self.screen.onkey(self.paddle2_on.move_down, key='s')
        game_on = True
        while game_on:
            self.screen.update()
        self.screen.exitonclick()


game = PongGame()
game.game_on()

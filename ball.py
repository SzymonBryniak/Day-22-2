from turtle import Screen, Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('Green')
        self.shapesize(1, 1)

    def move_ball(self):
        self.speed(1)
        self.goto(380, 280)

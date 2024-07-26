from turtle import Screen, Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('Green')
        self.shapesize(1, 1)
        self.goto(position)

    def move_ball(self):
        self.goto(260, 40)

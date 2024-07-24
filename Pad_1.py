from turtle import Screen, Turtle


class Paddle1(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('Green')
        self.shapesize(5, 1)
        self.goto(position)

    def move_up(self):
        # Paddle.setheading(90)
        up_cor = self.ycor() + 10
        self.goto(x=350, y=up_cor)
        return self

    def move_down(self):
        # Paddle.setheading(90)
        down_cor = self.ycor() - 10
        self.goto(x=350, y=down_cor)
        return self

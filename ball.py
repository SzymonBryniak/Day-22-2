from turtle import Screen, Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('Green')
        self.shapesize(1, 1)

    def move_ball(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        # self.speed(1)
        self.goto(new_x, new_y)

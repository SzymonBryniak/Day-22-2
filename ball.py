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
        if new_x - 5 >= 290:
            return
        else:
            self.goto(new_x, new_y)
            print(self.xcor())

    def move_ball_udemy(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        return new_x, new_y



from turtle import Screen, Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('Green')
        self.shapesize(1, 1)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        if new_x >= 290:
            while new_y < 300:
                new_y = self.ycor() - 10
                self.goto(new_x, new_y)
                return
        else:

            self.goto(new_x, new_y)
            print(self.xcor(), self.ycor())
            return

    def bounce_udemy(self):
        self.y_move *= -1

    def move_ball_udemy(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)




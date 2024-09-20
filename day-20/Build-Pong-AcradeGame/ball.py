from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5  # Increased speed for faster movement
        self.y_move = 5  # Increased speed for faster movement
        self.move_speed = 0.05  # Decreased initial speed for faster ball movements

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1  # Reverse Y direction

    def bounce_x(self):
        self.x_move *= -1  # Reverse X direction
        self.move_speed *= 0.9  # Increase ball speed after hitting a paddle

    def reset_position(self):
        self.goto(0, 0)  # Reset ball position to center
        self.move_speed = 0.05  # Reset speed to initial value after a point
        self.bounce_x()  # Change direction when resetting position

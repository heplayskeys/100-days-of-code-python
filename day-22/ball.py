from random import choice, randint
from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__(shape="circle")
    self.color("white")
    self.penup()
    self.x_move = 4
    self.y_move = 1.5

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto((new_x, new_y))

  def bounce_y(self):
    if self.ycor() > 285:
      self.goto(self.xcor(), 285)
    elif self.ycor() < -280:
      self.goto(self.xcor(), -280)
    self.y_move *= -1

  def bounce_x(self):
    self.x_move *= -1
    # if not self.x_move in (-6, -1, 1, 6):
    #   self.x_move += randint(-1, 1)

  def goal(self):
    self.goto(0, 0)
    self.x_move *= -1
    if self.x_move < -4:
      self.x_move = -4
    elif self.x_move > 4:
      self.x_move = 4
    self.y_move = 1.5


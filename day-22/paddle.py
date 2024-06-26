from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, pos=(350, 0)):
    super().__init__(shape="square")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.color("white")
    self.penup()
    self.goto(pos)

  def move_up(self):
    if self.ycor() < 241:
      new_y = self.ycor() + 20
      self.goto(self.xcor(), new_y)

  def move_down(self):
    if self.ycor() > -240:
      new_y = self.ycor() - 20
      self.goto(self.xcor(), new_y)
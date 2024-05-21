from turtle import Turtle

COLOR = "white"
MOVE_DISTANCE = 20
SHAPE = "square"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
  def __init__(self, size=3):
    self.body = []
    self.create_snake(size)
    self.head = self.body[0]
  
  def create_snake(self, size):
    for x in range(0, -(MOVE_DISTANCE * size) + 1, -MOVE_DISTANCE):
      self.add_to_body(x)
  
  def add_to_body(self, x, y=0):
      s = Turtle(shape=SHAPE)
      s.color(COLOR)
      s.penup()
      s.goto(x=x, y=y)
      self.body.append(s)
  
  def grow(self):
    x, y = self.body[-1].position()
    self.add_to_body(x, y)
  
  def move(self):
    for s in range(len(self.body) - 1, 0, -1):
      x_pos = self.body[s - 1].xcor()
      y_pos = self.body[s - 1].ycor()
      self.body[s].goto(x_pos, y_pos)
    self.head.forward(MOVE_DISTANCE)

  def moving_dir(self):
    return self.head.heading()

  def up(self):
    if self.moving_dir() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.moving_dir() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.moving_dir() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.moving_dir() != LEFT:
      self.head.setheading(RIGHT)

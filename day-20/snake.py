from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
  def __init__(self, size=3):
    self.snake = self.create_snake(size)
    self.head = self.snake[0]
  
  def create_snake(self, size):
    snake = []
    for x in range(0, -(MOVE_DISTANCE * size) + 1, -MOVE_DISTANCE):
      s = Turtle(shape="square")
      s.color("white")
      s.penup()
      s.goto(x=x, y=0)
      snake.append(s)
    return snake
  
  def move(self):
    for s in range(len(self.snake) - 1, 0, -1):
      x_pos = self.snake[s - 1].xcor()
      y_pos = self.snake[s - 1].ycor()
      self.snake[s].goto(x_pos, y_pos)
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

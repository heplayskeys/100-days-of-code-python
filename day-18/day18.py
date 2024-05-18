import colorgram as cg
import turtle as turtle_module
from random import choice

COLORS = cg.extract("image.jpg", 30)
RGB_COLORS = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in COLORS]
COLOR_LIST = [c for c in RGB_COLORS if sum(c) < 700]
DOTS_PER_ROW = 13
DOT_ROWS = DOTS_PER_ROW
DOT_SIZE = 20
DOT_SPACE = 50

turtle_module.colormode(255)

turtle = turtle_module.Turtle()
turtle.hideturtle()
turtle.penup()
turtle.speed("fastest")
canvas = turtle_module.Screen()

def paint_across(step):
  start_pos = 300
  turtle.teleport(-start_pos - 7.5, -start_pos + step)

  for dot_num in range(DOTS_PER_ROW):
    turtle.color(choice(COLOR_LIST))
    turtle.dot(DOT_SIZE)
    if dot_num < DOTS_PER_ROW - 1:
      turtle.forward(DOT_SPACE)

for row in range(DOT_ROWS):
  step = row * DOT_SPACE
  paint_across(step)

canvas.exitonclick()
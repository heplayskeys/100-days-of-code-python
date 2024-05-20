from random import choice, randint
from turtle import Turtle, Screen

colors = {
  "red": "r",
  "orange": "o",
  "yellow": "y",
  "green": "g",
  "blue": "b",
  "indigo": "i",
  "violet": "v",
}

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place Your Bet", prompt="Which color turtle will win the race? Enter a color (R, O, Y, G, B, I, V): ").lower()

turtles = []
for color in colors:
  turtle = Turtle(shape="turtle")
  turtle.color(color)
  turtle.speed(7)
  turtle.penup()
  turtles.append(turtle)

lane_height = (screen.canvheight // len(turtles))
starting_x = -(screen.canvwidth / 2)
starting_y = -lane_height * (len(turtles) // 2)

for lane in range(len(turtles)):
  turtles[lane].goto(starting_x, starting_y + (lane * lane_height))

racing = True
while racing:
  turtle = choice(turtles)
  turtle.forward(randint(0, 10))
  if turtle.xcor() > (screen.canvwidth / 2) + 50:
    winner = turtle.fillcolor()
    racing = False

if bet == colors[winner]:
  print(f"You Win! The winning turtle is {winner}!")
else:
  print(f"You Lose. The winning turtle was {winner}.")

screen.exitonclick()




### Turtle Sketch Logic (below)

# tubby = Turtle()
# tubby.speed(8)
# screen = Screen()

# def move_forward():
#   tubby.forward(10)

# def move_backward():
#   tubby.backward(10)

# def turn_left():
#   tubby.left(10)

# def turn_right():
#   tubby.right(10)

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=screen.reset)

# screen.exitonclick()
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_playing = True
while is_playing:
  screen.update()
  time.sleep(0.1)
  snake.move()

  # Detect collision with food
  if snake.head.distance(food) < 10:
    food.refresh()
    scoreboard.increase_score()
    snake.grow()

  # Detect collision with wall
  if snake.head.xcor() > 295 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
    is_playing = False
    scoreboard.game_over()

  # Detect collision with tail
  for s in snake.body[1:]:
    if snake.head.distance(s) < 10:
      is_playing = False
      scoreboard.game_over()

screen.exitonclick()

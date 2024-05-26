from ball import Ball
from paddle import Paddle
from random import randint
from scoreboard import Scoreboard
from turtle import Screen
import time

L_START = (-350, 0)
R_START = (350, 0)

gameboard = Screen()
gameboard.bgcolor("black")
gameboard.setup(width=800, height=600)
gameboard.title("Pong")
gameboard.tracer(0)

r_paddle = Paddle(pos=R_START)
l_paddle = Paddle(pos=L_START)
ball = Ball()
scoreboard = Scoreboard()

gameboard.listen()
gameboard.onkey(r_paddle.move_up, "Up")
gameboard.onkey(r_paddle.move_down, "Down")
gameboard.onkey(l_paddle.move_up, "w")
gameboard.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
  if ball.ycor() > 285 or ball.ycor() < -280:
    ball.bounce_y()
  
  if (-330 < ball.xcor() < -325 and ball.distance(l_paddle) < 50) or (325 < ball.xcor() < 330 and ball.distance(r_paddle) < 50):
    ball.bounce_x()

  if ball.xcor() < -420:
    scoreboard.r_point()
    ball.goal()
    r_paddle.goto(R_START)
    l_paddle.goto(L_START)
    time.sleep(0.125) 

  if ball.xcor() > 420:
    scoreboard.l_point()
    ball.goal()
    r_paddle.goto(R_START)
    l_paddle.goto(L_START)   
    time.sleep(0.125)

  ball.move()
  gameboard.update()

gameboard.exitonclick()

from turtle import Turtle

CENTER_ALIGN = "center"
FONT = ("Courier New", 24, "normal")
FONT_COLOR = "white"

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__(visible=False)
    self.score = 0
    self.penup()
    self.color(FONT_COLOR)
    self.goto(0, 270)
    self.update()

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=CENTER_ALIGN, font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update()

  def update(self):
    self.write(f"Score: {self.score}", align=CENTER_ALIGN, font=FONT)


from turtle import Turtle
ALIGNMENT = "center"
FONT = ( 'Times new Roman', 18, 'normal')
class Score(Turtle):

     def __init__(self):
         super().__init__()
         self.score = 0
         self.color("white")
         self.penup()
         self.goto(0, 267)
         self.write(f"Score: {self.score}",move = False, align = ALIGNMENT, font = FONT)
         self.hideturtle()

     def game_over(self):
         self.goto(0,0)
         self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
     def increase_score(self):
         self.clear()
         self.score += 1
         self.write(f"Score: {self.score}", move=False, align="center", font=('Times new Roman', 18, 'normal'))
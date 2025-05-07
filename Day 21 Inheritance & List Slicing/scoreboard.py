from turtle import Turtle
CONSTANT_POSITION = (0, 270)
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(CONSTANT_POSITION)
        self.color("white")
        self.score = 0
        self.text = f"SCORE = {self.score}"
        self.write(arg=self.text, move=False, align=ALIGNMENT, font=FONT )
    def point(self):
        self.clear()
        self.score += 1
        self.text = f"SCORE = {self.score}"
        self.write(arg=self.text, move=False, align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)


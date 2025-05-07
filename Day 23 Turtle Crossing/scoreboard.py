from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-230, 230)
        self.write(f" Level: {self.level}", align="center",font=FONT)
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f" Level: {self.level}", align="center", font=FONT)
    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)




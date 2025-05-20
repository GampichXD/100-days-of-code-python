# Professional Portfolio Project - Game
# Breakout Game
# Author : Abraham
import turtle
import time
import random

# Set up screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 3
ball.dy = 3

# Bricks
bricks = []

colors = ["red", "orange", "green", "yellow"]
for y in range(250, 150, -30):
    for x in range(-350, 400, 70):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(colors))
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# Paddle movement
def go_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 40)

def go_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 40)

screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Game loop
while True:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Wall collision
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1
    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() < -230 and ball.ycor() > -240) and (abs(ball.xcor() - paddle.xcor()) < 50):
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if ball.distance(brick) < 35:
            ball.dy *= -1
            brick.goto(1000, 1000)
            bricks.remove(brick)
            break

    # Missed ball
    if ball.ycor() < -300:
        time.sleep(1)
        ball.goto(0, -200)
        ball.dx = 3 * random.choice([-1, 1])
        ball.dy = 3

    # Game Over
    if not bricks:
        ball.hideturtle()
        paddle.hideturtle()
        screen.clear()
        screen.bgcolor("black")
        turtle.write("YOU WIN!", align="center", font=("Courier", 36, "bold"))
        break

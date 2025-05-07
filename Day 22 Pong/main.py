
"""
- Score
- Ball
- Player

1. Create the screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses
8. Keep score
"""

# Step 1 : Create the screen
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")


screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

# Step 2 : Create and move a paddle
# width = 5
# height = 1
# x_pos = 350
# y_pos = 0
# paddle = Turtle(shape="square")
# paddle.penup()
# paddle.goto(x = x_pos,y = y_pos)
# paddle.color("white")
# paddle.shapesize(stretch_wid=width,stretch_len=height)

#
# def up_pad():
#     # screen.tracer(0)
#     # paddle.setheading(90)
#     # paddle.forward(20)
#     # paddle.setheading(0)
#     # screen.update()
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
# def down_pad():
#     # screen.tracer()
#     # paddle.setheading(270)
#     # paddle.forward(20)
#     # paddle.setheading(0)
#     # screen.update()
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen.listen()

screen.onkey(fun = r_paddle.go_up, key = "Up")
screen.onkey(fun = r_paddle.go_down, key = "Down")
screen.onkey(fun = l_paddle.go_up, key = "w")
screen.onkey(fun = l_paddle.go_down, key = "s")


# screen.update()




game_is_on = True

while game_is_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        # ball.x_move += 1
        # ball.y_move += 1


    if ball.xcor() > 380 :
        ball.restart()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()
    if scoreboard.r_score == 10 or scoreboard.l_score == 10:
        print("Thanks For Playing")
        game_is_on = False







screen.exitonclick()












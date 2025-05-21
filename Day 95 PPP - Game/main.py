# Professional Portfolio Project - Game
# Space Invaders
# Author : Abraham
import turtle
import time
import random
import math

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders")
win.setup(width=600, height=600)

# Register shapes
win.register_shape("invader_small.gif")
win.register_shape("spaceship.gif")

# Score display
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-250, 260)
score_display.write(f"Score: {score}", font=("Arial", 14, "normal"))

# Player
player = turtle.Turtle()
player.shape("spaceship.gif")
player.penup()
player.goto(0, -250)
player.setheading(90)
player_speed = 15

# Bullet
bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready"

# Enemy setup
num_enemies = 5
enemies = []

for i in range(num_enemies):
    enemy = turtle.Turtle()
    enemy.shape("invader_small.gif")
    enemy.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

enemy_speed = 5

# Move player
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -270:
        x = -270
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 270:
        x = 270
    player.setx(x)

# Fire bullet
def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()

# Collision detection
def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    return distance < 20

# Keyboard bindings
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onkeypress(fire_bullet, "space")

# Main game loop
game_running = True
while game_running:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Reverse and move down
        if enemy.xcor() > 270 or enemy.xcor() < -270:
            enemy_speed *= -1
            for e in enemies:
                e.sety(e.ycor() - 30)

        # Check for game over
        if enemy.ycor() < -230:
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
            print("GAME OVER")
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            game_running = False
            break

        # Check for collision
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(150, 250)
            enemy.goto(x, y)
            score += 10
            score_display.clear()
            score_display.goto(-250, 260)
            score_display.write(f"Score: {score}", font=("Arial", 14, "normal"))

    # Move bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Bullet reset
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    time.sleep(0.02)

# Keep window open
win.mainloop()

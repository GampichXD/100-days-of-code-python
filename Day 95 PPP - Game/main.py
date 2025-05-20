import turtle
import time
import random
import math
import os

# --- Setup Window ---
win = turtle.Screen()
win.bgcolor("black")
win.title("Space Invaders PNG Edition")
win.setup(width=600, height=600)
win.tracer(0)  # Turn off animation for faster drawing

# --- Register PNG images ---
# Convert .png to .gif temporarily if needed using Pillow, but Turtle 3.7+ supports PNG
try:
    win.register_shape("player.png")
    win.register_shape("enemy.png")
except:
    print("Make sure your PNGs are in the correct path and compatible.")

# --- Score Display ---
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("white")
score_display.goto(-250, 260)
score_display.write(f"Score: {score}", font=("Arial", 14, "normal"))

# --- Player ---
player = turtle.Turtle()
player.shape("player.png")
player.penup()
player.goto(0, -250)
player.setheading(90)
player_speed = 20

# --- Bullet ---
bullet = turtle.Turtle()
bullet.shape("circle")
bullet.color("yellow")
bullet.shapesize(0.3, 0.3)
bullet.penup()
bullet.hideturtle()
bullet.setheading(90)
bullet_speed = 25
bullet_state = "ready"

# --- Enemies ---
num_enemies = 6
enemies = []

for _ in range(num_enemies):
    enemy = turtle.Turtle()
    enemy.shape("enemy.png")
    enemy.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.goto(x, y)
    enemies.append(enemy)

enemy_speed = 5

# --- Functions ---

def move_left():
    x = player.xcor() - player_speed
    if x < -270:
        x = -270
    player.setx(x)

def move_right():
    x = player.xcor() + player_speed
    if x > 270:
        x = 270
    player.setx(x)

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()

def is_collision(t1, t2):
    return t1.distance(t2) < 20

# --- Controls ---
win.listen()
win.onkeypress(move_left, "Left")
win.onkeypress(move_right, "Right")
win.onkeypress(fire_bullet, "space")

# --- Game Loop ---
game_over = False

while not game_over:
    win.update()

    for enemy in enemies:
        x = enemy.xcor() + enemy_speed
        enemy.setx(x)

        # Bounce
        if enemy.xcor() > 270 or enemy.xcor() < -270:
            enemy_speed *= -1
            for e in enemies:
                e.sety(e.ycor() - 30)

        # Collision with player
        if enemy.ycor() < -230:
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
            score_display.goto(0, 0)
            score_display.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            game_over = True
            break

        # Collision with bullet
        if is_collision(bullet, enemy):
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.goto(0, -400)
            enemy.goto(random.randint(-200, 200), random.randint(150, 250))
            score += 10
            score_display.clear()
            score_display.goto(-250, 260)
            score_display.write(f"Score: {score}", font=("Arial", 14, "normal"))

    # Move bullet
    if bullet_state == "fire":
        y = bullet.ycor() + bullet_speed
        bullet.sety(y)

    # Bullet off-screen
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

    time.sleep(0.02)

win.mainloop()

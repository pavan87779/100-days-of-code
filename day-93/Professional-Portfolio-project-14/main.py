import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.tracer(0)

# Player setup
player = turtle.Turtle()
player.shape("square")
player.color("green")
player.shapesize(stretch_wid=1, stretch_len=2)
player.penup()
player.goto(0, -250)

# Movement speed
player_speed = 15

# Bullet setup
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.5, stretch_len=1)
bullet.penup()
bullet.hideturtle()
bullet_speed = 20

# Alien setup
aliens = []
alien_speed = 0.1

# Create aliens
def create_aliens():
    for _ in range(6):
        alien = turtle.Turtle()
        alien.shape("square")
        alien.color("red")
        alien.penup()
        alien.speed(0)
        x = random.randint(-300, 300)
        y = random.randint(100, 250)
        alien.goto(x, y)
        aliens.append(alien)

# Move the player
def move_left():
    x = player.xcor()
    if x > -350:
        player.setx(x - player_speed)

def move_right():
    x = player.xcor()
    if x < 350:
        player.setx(x + player_speed)

# Shoot bullet
def shoot_bullet():
    if not bullet.isvisible():
        bullet.goto(player.xcor(), player.ycor() + 20)
        bullet.showturtle()

# Check for collision between bullet and aliens
def check_collision():
    global score
    for alien in aliens:
        if bullet.distance(alien) < 20:
            alien.goto(random.randint(-300, 300), random.randint(100, 250))
            bullet.hidet()
            score += 1
            update_score()

# Move aliens
def move_aliens():
    for alien in aliens:
        x = alien.xcor()
        x += random.choice([-alien_speed, alien_speed])
        alien.setx(x)

# Update score
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 270)
score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}", font=("Arial", 16, "normal"))

# Check for game over (if any alien touches the player)
def check_game_over():
    for alien in aliens:
        if alien.ycor() < -250:
            game_over()

def game_over():
    global running
    running = False
    game_over_text = turtle.Turtle()
    game_over_text.color("red")
    game_over_text.penup()
    game_over_text.hideturtle()
    game_over_text.goto(0, 0)
    game_over_text.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(shoot_bullet, "space")

# Main game loop
running = True
create_aliens()

# Make sure screen stays open until the user closes it
while running:
    screen.update()
    move_aliens()
    check_collision()
    check_game_over()
    time.sleep(0.01)

# Close the screen when clicked
screen.bye()

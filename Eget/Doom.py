import turtle
import math
import random

# Screen setup
screen = turtle.Screen()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Player setup
player = turtle.Turtle()
player.shape("triangle")
player.shapesize(1, 1.5)
player.color("white")
player.penup()
player.speed(0)
player.goto(-100, 0)
player_angle = 0
player_speed = 10

def create_enemies(num):
    enemies = []
    for _ in range(num):
        enemy = turtle.Turtle()
        enemy.shape("circle")
        enemy.color("red")
        enemy.penup()
        enemy.speed(0)
        enemy.goto(random.randint(-SCREEN_WIDTH//2 + 50, SCREEN_WIDTH//2 - 50), 
                   random.randint(-SCREEN_HEIGHT//2 + 50, SCREEN_HEIGHT//2 - 50))
        enemies.append(enemy)
    return enemies

enemies = create_enemies(3)

def check_enemy_collision():
    global enemies
    for enemy in enemies:
        if enemy.isvisible() and player.distance(enemy) < 20:
            enemy.hideturtle()
            print("Enemy defeated!")
    if all(not enemy.isvisible() for enemy in enemies):
        reset_game()

# Map setup
walls = []
TILE_SIZE = 50
MAP_WIDTH = SCREEN_WIDTH // TILE_SIZE
MAP_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

def generate_random_map():
    map_data = []
    for row in range(MAP_HEIGHT):
        if row == 0 or row == MAP_HEIGHT - 1:
            map_data.append("#" * MAP_WIDTH)
        else:
            row_data = "#"
            for col in range(1, MAP_WIDTH - 1):
                row_data += "#" if random.random() < 0.2 else " "
            row_data += "#"
            map_data.append(row_data)
    return map_data

def draw_map():
    global walls, map_data
    walls.clear()
    wall_turtle = turtle.Turtle()
    wall_turtle.shape("square")
    wall_turtle.color("gray")
    wall_turtle.penup()
    map_data = generate_random_map()
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            if map_data[row][col] == "#":
                x = (col - len(map_data[0]) / 2) * TILE_SIZE
                y = (len(map_data) / 2 - row) * TILE_SIZE
                wall_turtle.goto(x, y)
                wall_turtle.stamp()
                walls.append((x, y))

def reset_game():
    global enemies
    print("New Level!")
    for enemy in enemies:
        enemy.hideturtle()
    enemies = create_enemies(random.randint(3, 5))
    draw_map()
    player.goto(-100, 0)

# Player movement
def move_forward():
    global player_angle
    new_x = player.xcor() + player_speed * math.cos(math.radians(player_angle))
    new_y = player.ycor() + player_speed * math.sin(math.radians(player_angle))
    if (new_x, new_y) not in walls:
        player.goto(new_x, new_y)

def move_backward():
    global player_angle
    new_x = player.xcor() - player_speed * math.cos(math.radians(player_angle))
    new_y = player.ycor() - player_speed * math.sin(math.radians(player_angle))
    if (new_x, new_y) not in walls:
        player.goto(new_x, new_y)

def turn_left():
    global player_angle
    player_angle -= 15
    player.setheading(player_angle)

def turn_right():
    global player_angle
    player_angle += 15
    player.setheading(player_angle)

# Shooting function
def shoot():
    bullet = turtle.Turtle()
    bullet.shape("square")
    bullet.color("yellow")
    bullet.penup()
    bullet.speed(0)
    bullet.goto(player.xcor(), player.ycor())
    bullet.setheading(player_angle)
    
    for _ in range(20):
        bullet.forward(15)
        for enemy in enemies:
            if enemy.isvisible() and bullet.distance(enemy) < 15:
                enemy.hideturtle()
                bullet.hideturtle()
                return
    bullet.hideturtle()

# Keyboard bindings
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(turn_left, "d")
screen.onkeypress(turn_right, "a")
screen.onkeypress(shoot, "space")

# Main loop
draw_map()
running = True
while running:
    check_enemy_collision()
    screen.update()

turtle.done()

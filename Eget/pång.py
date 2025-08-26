import random
import turtle

# Skapa skärmen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0)  # Stäng av automatisk uppdatering

# Skapa paddlar och boll
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.fillcolor("blue")
t2.fillcolor("red")
t3.fillcolor("yellow")

lista = [t1, t2, t3]
lista2 = [t1, t2]

for i in lista:
    i.penup()
for y in lista2:
    y.shape("square")
    y.shapesize(4, 0.5)
t3.shape("circle")

t1.goto(-350, 0)
t2.goto(350, 0)

# Bollens hastighet i x- och y-led
speed_x = random.choice([-3, 3])
speed_y = random.choice([-3, 3])

# Funktion för att invertera hastighet
def invert(axis):
    global speed_x, speed_y
    if axis == "x":
        speed_x = -speed_x
    elif axis == "y":
        speed_y = -speed_y

# Rörelsefunktioner för paddlar
def upåt():
    if t1.ycor() < 250:
        t1.sety(t1.ycor() + 20)

def neråt():
    if t1.ycor() > -250:
        t1.sety(t1.ycor() - 20)

def upåt2():
    if t2.ycor() < 250:
        t2.sety(t2.ycor() + 20)

def neråt2():
    if t2.ycor() > -250:
        t2.sety(t2.ycor() - 20)

screen.listen()
screen.onkey(upåt, "q")
screen.onkey(neråt, "a")
screen.onkey(upåt2, "p")
screen.onkey(neråt2, "l")

# Bollens rörelse
def move_ball():
    global speed_x, speed_y

    # Uppdatera bollens position
    t3.setx(t3.xcor() + speed_x)
    t3.sety(t3.ycor() + speed_y)

    # Kolla kollision med väggar (top & bottom)
    if t3.ycor() > 290 or t3.ycor() < -290:
        invert("y")  # Invertera y-riktning

    # Kolla kollision med paddlar
    if (t3.xcor() < -340 and t3.xcor() > -350 and abs(t3.ycor() - t1.ycor()) < 50) or \
       (t3.xcor() > 340 and t3.xcor() < 350 and abs(t3.ycor() - t2.ycor()) < 50):
        invert("x")  # Invertera x-riktning

    screen.update()  # Uppdatera skärmen
    screen.ontimer(move_ball, 10)  # Anropa igen efter 10ms

# Starta bollens rörelse
move_ball()

turtle.done()

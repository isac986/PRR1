import random
import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()

t1.fillcolor("blue")
t2.fillcolor("red")
t3.fillcolor("yellow")

lista = [t1, t2, t3, t4]
spelare = [t1, t2]

for i in lista:
    i.penup()
for y in spelare:
    y.shape("square")
    y.shapesize(3, 0.5)
t3.shape("circle")
    
t1.goto(-350, 0)
t2.goto(350, 0)
t4.goto(0, 0)
t4.hideturtle()

# Rörelse
def upåt():
    y = t1.ycor() + 13
    t1.goto(-350, y)

def neråt():
    y = t1.ycor() - 13
    t1.goto(-350,y)

def upåt2():
    y = t2.ycor() + 13
    t2.goto(350, y)
    
def neråt2():
    y = t2.ycor() - 13
    t2.goto(350, y)


bollen = True
x_speed = 2
y_speed = 2

def bollen():
    global x_speed, y_speed
    x = t3.xcor() + x_speed
    y = t3.ycor() + y_speed

    t3.goto(x,y)
    
    if t3.ycor() == 300 or t3.ycor() == -300:
        y_speed = y_speed * -1
    
    elif t3.distance(t2.pos()) <= 20 and t3.xcor() >= t2.xcor():
        if(t3.ycor() >= t2.ycor() + 2 or t3.ycor() <= t2.ycor() - 2):
            x_speed = x_speed * -1
        
    elif t3.distance(t1.pos()) <= 20:
        x_speed = x_speed * -1
         
    elif t3.xcor() == 400:
        t4.write("Blå är vinnare",False,"center",("Ariel",30,"normal"))
        turtle.done()
        
    elif t3.xcor() == -400:
        t4.write("Röd är vinnare")
        turtle.done()
     
while True:
    screen.listen()
    screen.onkey(upåt, "q")
    screen.onkey(neråt, "a")
    screen.onkey(upåt2, "p")
    screen.onkey(neråt2, "l")
    bollen()
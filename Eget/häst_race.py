import random
import turtle

screen = turtle.Screen()
screen.setup(width=1000, height=600)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()

lista = [t1, t2, t3, t4, t5]

t1.fillcolor("blue")
t2.fillcolor("purple")
t3.fillcolor("yellow")
t4.fillcolor("green")
t5.fillcolor("pink") 
t6.pencolor("red")

for i in lista:
    i.penup()
    i.shape("turtle")

t6.penup()
t6.goto(350, 300)
t6.pendown()
t6.goto(350, -300)
t6.hideturtle()

t1.goto(-400, -90)
t2.goto(-400, -60)
t3.goto(-400, -30)
t4.goto(-400, 0)
t5.goto(-400, 30)

tävling = True
vinnare = None

while tävling:
    for i in lista:
        if i == t5:  
            i.forward(random.randint(5, 20))
        else:
            i.forward(random.randint(1, 11))

        if i.xcor() >= 350:
            tävling = False
            vinnare = i.fillcolor()
            break

print(f"Vinnaren är sköldpaddan med färgen {vinnare}!")

turtle.done()

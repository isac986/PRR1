import turtle
screen =turtle.Screen()
screen.setup(width=800, height=600)
t = turtle.Turtle()

t.pensize(6)
t.speed(0)
t.goto(-100, 0)

for i in range(10):
    t.color("red")
    t.forward(120)
    t.right(80)
    for y in range(8):
        t.color("blue")
        t.forward(100)
        t.right(40)

turtle.done()
import turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()

for i in range(1, 25):
    t.forward(100)
    t.left(90)
    
    if i % 4 == 0:
        t.left(60)
        
turtle.done()
import turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)

t = turtle.Turtle()

def stjärna(uddar):
    for i in range(9):
        t.forward(100)
        t.right(60 / uddar + 160)
        
stjärna(18)

turtle.done()
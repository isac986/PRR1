import turtle
screen = turtle.Screen()
screen.setup(width=800, height=600)

t = turtle.Turtle()

t.speed(0)

t.penup()
t.goto(-70, 0)
t.pendown()

def draw_fractal(t, length, depth):

    if depth == 0:
        t.forward(length)
    else: 
        for angle in [75, -120, 75, 0]:
            draw_fractal(t, length / 3, depth - 1)
            t.left(angle)

for _ in range(4):
    draw_fractal(t, 600, 4)
    t.right(120)

turtle.done()
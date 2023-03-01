import turtle as t
from random import randint, random
t.speed('fastest')

def draw_star(points, size, col, x, y ):
    t.penup()
    t.goto(x,y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()


t.Screen().bgcolor('dark blue')
while True:
    ranPts = randint(2,7) * 2 + 1
    ranSize = randint(10,50)
    ranCol = (random(), random(), random())
    ranX = randint(-450, 400)
    ranY = randint(-350, 350)
    draw_star(ranPts,ranSize,ranCol,ranX,ranY)

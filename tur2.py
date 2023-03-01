import turtle
from itertools import cycle
from tkinter import Tk
colors = cycle(['red','orange','yellow','green','blue','maroon','purple'])

Tk()

def draw_circle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    draw_circle(size+5)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)

draw_circle(30)

from tkinter import Tk, Canvas
import datetime
root = Tk()
c = Canvas(root, width=800, height = 80, bg = 'black')
c.pack()
c.create_text(100,50,anchor='w', fill='orange',font = 'Arial 28 bold', text ='My cal')

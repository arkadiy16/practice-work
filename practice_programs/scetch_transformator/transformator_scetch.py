import turtle
import logging
from tkinter import *
from tkinter import ttk
from PIL import Image


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')

s = turtle.getscreen()
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def rect(width, lenght):
    for forw in 2 * (width, lenght):
        t.fd(forw)
        t.rt(90)


def coil(c_l, a1, a12, a2, a_, l):
    c_w = 2 * (a1 + a12 + a2)
    rect(c_w, c_l)
    t.penup()
    tp = t.pos()
    t.goto(tp[0] + a1 + a12 + a2 - a_, tp[1] - (c_l - l) / 2)
    t.pendown()
    rect(a1 + a12 + a2, l)
    t.fd(a2)
    rect(a12, l)


def scetch(*args):
    try:
        d1_s =98 #float(d1_entry.get())  #
        a1_s =27.5 #float(a1_entry.get())  # 27.5
        a2_s =15# float(a12_entry.get())  # 15
        a12_s =10# float(a2_entry.get())  # 10
        l_s = 282#float(l_entry.get())  # 282
        d_s = 90#float(d_entry.get())  # 90
        hc_s = 320#float(hc_entry.get())  # 320
        hi_s = 85#float(hi_entry.get())  # 85
        c_s = 213#float(c_entry.get())  # 213
    except ValueError:
        return

    t.penup()
    t.goto(-c_s - (hi_s - d_s / 2), hc_s / 2 + hi_s)
    t.pendown()
    rect(2 * c_s + 2 * (hi_s - d_s / 2), hc_s + 2 * hi_s)  # outer rect

    t.penup()
    tp = t.pos()
    t.goto(tp[0] + hi_s / 2 + d_s / 2, tp[1] - hi_s)
    t.pendown()

    coil(hc_s, a1_s, a12_s, a2_s, (d1_s - d_s) / 2, l_s)

    t.penup()
    t.goto(c_s - d_s / 2, - hc_s / 2)
    t.pendown()
    coil(-hc_s, -a1_s, -a12_s, -a2_s, -(d1_s - d_s) / 2, -l_s)

    screen = turtle.getscreen()
    screen.setup(1000, 1000)
    screen.getcanvas().postscript(file='12.eps', width=1000, height=1000)
    with Image.open('12.png') as f:
        screen.getcanvas().convert('png').save('121.png')


root = Tk()
root.title('Transformator scetch')

mainframe = ttk.Frame(root, padding='3 9 100 100')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

d1, a1, a12, a2, l, d, hc, hi, c = (StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(),
                                    StringVar(), StringVar(), StringVar())

# Cells for entry variables.
d1_entry = ttk.Entry(mainframe, width=8, textvariable=d1)
a1_entry = ttk.Entry(mainframe, width=8, textvariable=a1)
a12_entry = ttk.Entry(mainframe, width=8, textvariable=a12)
a2_entry = ttk.Entry(mainframe, width=8, textvariable=a2)
l_entry = ttk.Entry(mainframe, width=8, textvariable=l)
d_entry = ttk.Entry(mainframe, width=8, textvariable=d)
hc_entry = ttk.Entry(mainframe, width=8, textvariable=hc)
hi_entry = ttk.Entry(mainframe, width=8, textvariable=hi)
c_entry = ttk.Entry(mainframe, width=8, textvariable=c)

# Variables cells arrangement.
d1_entry.grid(column=0, row=1, sticky=W+E)
a1_entry.grid(column=1, row=1, sticky=W+E)
a12_entry.grid(column=2, row=1, sticky=W+E)
a2_entry.grid(column=3, row=1, sticky=W+E)
l_entry.grid(column=4, row=1, sticky=W+E)
d_entry.grid(column=5, row=1, sticky=W+E)
hc_entry.grid(column=6, row=1, sticky=W+E)
hi_entry.grid(column=7, row=1, sticky=W+E)
c_entry.grid(column=8, row=1, sticky=W+E)

# Cells for variables labels.
ttk.Label(mainframe, text='d1, mm').grid(column=0, row=0, sticky=W)
ttk.Label(mainframe, text='a1, mm').grid(column=1, row=0, sticky=W)
ttk.Label(mainframe, text='a12, mm').grid(column=2, row=0, sticky=W)
ttk.Label(mainframe, text='a2, mm').grid(column=3, row=0, sticky=W)
ttk.Label(mainframe, text='l, mm').grid(column=4, row=0, sticky=W)
ttk.Label(mainframe, text='d, mm').grid(column=5, row=0, sticky=W)
ttk.Label(mainframe, text='hc, mm').grid(column=6, row=0, sticky=W)
ttk.Label(mainframe, text='hi, mm').grid(column=7, row=0, sticky=W)
ttk.Label(mainframe, text='c, mm').grid(column=8, row=0, sticky=W)

ttk.Button(mainframe, text='Paint', command=scetch).grid(column=8, row=3, sticky=E)

d1_entry.focus()  # Focus cursor on field d1.
root.bind('<Return>', scetch)



root.mainloop()

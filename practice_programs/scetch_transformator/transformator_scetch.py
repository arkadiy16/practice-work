import turtle

s = turtle.getscreen()
t = turtle.Turtle()

t.penup()
t.setpos(-400, 300)
t.pendown()

def coil():
    pass

def outer_rect(lenght, width):
    for forw in 2 * (lenght, width):
        t.fd(forw)
        t.rt(90)

def main():
    d1 = 98
    a1 = 27.5
    a2 = 15
    a12 = 10
    l = 282
    d = 90
    hc = 320
    hi = 85
    c = 213
    outer_rect(2 * c + 2 * (hi - d / 2), hc + 2 * hi)
    input()



main()
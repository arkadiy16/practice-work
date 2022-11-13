import turtle

s = turtle.getscreen()
t = turtle.Turtle()


def coil(c_l, a1, a12, a2, a_, l):
    c_w = 2 * (a1 + a12 + a2)
    for forw in 2 * (c_w, c_l):
        t.fd(forw)
        t.rt(90)
    t.penup()
    tp = t.pos()
    t.goto(tp[0] + a1 + a12 + a2 - a_, tp[1] - (c_l - l) / 2)
    t.pendown()
    for forw in 2 * (a1 + a12 + a2, l):
        t.fd(forw)
        t.rt(90)
    t.fd(a2)
    t.rt(90)
    t.fd(l)
    t.rt(-90)
    t.fd(a12)
    t.rt(-90)
    t.fd(l)
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

    t.penup()
    t.goto(-c - (hi - d / 2), hc / 2 + hi)
    t.pendown()

    outer_rect(2 * c + 2 * (hi - d / 2), hc + 2 * hi)

    t.penup()
    tp = t.pos()
    t.goto(tp[0] + hi / 2 + d / 2, tp[1] - hi)
    t.pendown()

    coil(hc, a1, a12, a2, (d1 - d) / 2, l)

    t.penup()
    t.goto(c - d / 2, - hc / 2)
    t.pendown()
    t.rt(90)
    coil(-hc, -a1, -a12, -a2, -(d1 - d) / 2, -l)

    input()

main()

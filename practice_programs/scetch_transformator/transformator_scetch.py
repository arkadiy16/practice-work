import turtle

s = turtle.getscreen()
t = turtle.Turtle()


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
    rect(2 * c + 2 * (hi - d / 2), hc + 2 * hi) # outer rect

    t.penup()
    tp = t.pos()
    t.goto(tp[0] + hi / 2 + d / 2, tp[1] - hi)
    t.pendown()

    coil(hc, a1, a12, a2, (d1 - d) / 2, l)

    t.penup()
    t.goto(c - d / 2, - hc / 2)
    t.pendown()
    coil(-hc, -a1, -a12, -a2, -(d1 - d) / 2, -l)

    input()


main()

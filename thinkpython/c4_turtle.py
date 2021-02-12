import turtle
from math import pi
bob = turtle.Turtle()


# def square(t, length=0):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
#         i += 1

def polygon(t, length=1.0, n=3):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
        i += 1


def circle(t, r):
    circumference = float(2 * pi * r)
    n = 50
    comprimento = float(circumference / n)
    polygon(t, n, comprimento)


print(bob)
# square(bob, 200)
polygon(bob, 40, 12)
circle(bob, 20)

turtle.mainloop()

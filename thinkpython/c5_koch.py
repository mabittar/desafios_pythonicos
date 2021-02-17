from __future__ import print_function, division

import turtle


def koch(t, n):
    """ Desenha a curva Koch com comprimento n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """ desenha o floco de nove."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


comprimento = int(
    input("Entre com o comprimento a ser desenhado (maior que 100!): "))

bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, comprimento)

turtle.mainloop()

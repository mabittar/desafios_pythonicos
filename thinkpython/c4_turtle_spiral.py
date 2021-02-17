import turtle

turtle.bgcolor("black")


def spiral(sides, trun, color, width):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.pensize(5)

    for n in range(sides):
        t.forward(n)
        t.right(trun)


spiral(150, 45, "green", 5)
turtle.mainloop()

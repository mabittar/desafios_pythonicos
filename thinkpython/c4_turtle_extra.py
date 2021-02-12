import turtle

bob = turtle.Turtle()
turtle.bgcolor("black")
bob.speed(5)
bob.color("yellow")
bob.pensize(5)

for i in range(8):
    bob.left(45)
    for i in range(8):
        bob.forward(100)
        bob.right(45)
bob.hideturtle()

print(bob)
turtle.mainloop()

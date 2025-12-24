# import turtle

from turtle import Turtle

t = Turtle()
# t.screen.exitonclick()

angle = 60

for i in ["blue", "red", "orange"]:
    t.color(i)
    angle += 30
    for j in range (4):
        t.forward(100)
        t.right(angle)
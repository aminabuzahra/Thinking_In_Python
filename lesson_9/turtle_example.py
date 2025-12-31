# import turtle
from turtle import Turtle

t = Turtle()

angle = 120

t.color("red")
t.speed(0)
for i in range(37):    
    t.right(10)
    for j in range(3):
        t.right(angle)
        t.forward(100)

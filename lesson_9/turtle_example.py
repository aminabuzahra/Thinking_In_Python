# import turtle
from turtle import Turtle

t = Turtle()

angle = 90

t.color("blue")
t.speed(0)
for i in range(37):    
    t.right(10)
    for j in range (4):
        t.right(angle)
        t.forward(100)

# import turtle
import random
from turtle import Turtle

t = Turtle()

angle = 120

colors = ["red", "green", "blue", "yellow", "pink", "black", "purple", "brown"]

t.speed(0)
for i in range(37):
    color = random.choice(colors)
    t.color(color)
    t.right(10)
    for j in range(3):
        t.right(angle)
        t.forward(100)

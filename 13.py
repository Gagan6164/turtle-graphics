from turtle import Turtle
from turtle import *
x = Turtle()
y = Turtle()
x.speed(0)
y.speed(0)
y.color('white')
for i in range (1000):
    y.circle(20)
    
    
    x.up()
    x.goto(i,0)
    x.down()
    y.up()
    y.goto(i-1,0)
    y.down()
    x.circle(20)

import turtle
from turtle import *
speed(0)
for i in range (500):
    fd(1)
    circle(i,360-i**(0.5))
    fd(5)
    rt(90)
    fd(2)

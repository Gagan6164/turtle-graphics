import time
from time import sleep
import turtle
from turtle import *
import random
turtle.speed(1500)
turtle.pensize(2)
color1 = ['red','blue','yellow','brown']
up()
goto(-300,-300)
down()
for i in range (1,1000):
    r = random.randint(10,25)
    a = random.randint(-14,14)
    b = random.randint(-12,12)
    bgcolor("black")
    color(color1[i%4])
    up()
    goto(50*a,50*b)
    down()
    begin_fill()
    circle(r,360)
    end_fill()
    #sleep(0.1)
    #if (i%5== 0):
     #   reset()
    
    
    
    
    
    
    

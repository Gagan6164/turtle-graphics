import turtle
from turtle import *
color("green")
up()
goto(0,-300)
down()
pensize(18)
lt(90)
fd(200)

for j in range (2,7,1):
    for i in range (2,j):
        pensize(18-2*j)
        lt(90/i)
        fd(200/i**(0.5))
        #if (i>3):
        bk(200/i**(0.5))
        #break
    
        rt(180/i)
    
        fd(200/i**(0.5))
    #update()
       # bk(200/i**(0.7))
       # lt(90/i)
    
    

import turtle
from turtle import *
up()
goto(-300,-300)
down()
pensize(50)
speed(0)
color1 = ['red','yellow','green','blue','brown','white']
for i in range (11):
    color(color1[i%5])
    fd(600)
    up()
    goto(-300,-300+50*(i+1))
    down()
pensize(25)
up()
goto(0,-300)
down()
color(color1[5])
circle(250)
rt(90)

bk(500)
up()
goto(0,-50)
down()

for j in range(1,3):
    lt(i*150*((-1)**(j)))
    fd(230)
    bk(230)

lt(60)
fd(230)
bk(230)
    
    
    

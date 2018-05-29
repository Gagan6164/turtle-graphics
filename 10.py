import turtle
from turtle import *
color1 = ['red','green','orange','blue','yellow','purple']

speed(0)
n = int(input('enter the no of sides-->'))
pensize(n**2)
for i in range (1,200):
    
    color(color1[i%6])
    fd(i)
    rt(359/n)
for j in range (1,n+1):
    color('white')
    
    lt(359/n)
    bk(200-j)

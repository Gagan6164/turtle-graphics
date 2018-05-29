from turtle import *
color('purple', 'cyan')
begin_fill()
speed(0)

while True:
    forward(200)
    left(170)
    if abs(pos())< 1:
        break

end_fill()
done()

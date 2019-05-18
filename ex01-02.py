##Page 25.
##EXERCISE 1-2: A CIRCLE OF SQUARES
##Write and run a function that draws 60 squares, turning right 5 degrees after
##each square. Use a loop! Your result should end up looking like this...


from turtle import *

speed(.1)

def square():
    for i in range(4):
        fd(100)
        rt(90)

for i in range(60):
    square()
    rt(5)

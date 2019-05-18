##Page 32.
##EXERCISE 1-5: TURTLE SPIRAL
##Make a function to draw 60 squares, turning 5 degrees after each square
##and making each successive square bigger. Start at a l e n g t h  of 5 and
##increment 5 units every square. It should look like this...

from turtle import *

speed(.1)
setup(500, 300)

def square(a=100):
    for i in range(4):
        fd(a)
        rt(90)

a = 5
for i in range(60):
    square(a)
    rt(5)
    a += 5

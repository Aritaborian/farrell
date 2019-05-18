##Page 27.
##EXERCISE 1-3: TRI AND TRI AGAIN
##Write a   t r i a n g l e ( )  function that will draw a triangle of a given “side length.”

from turtle import *

def triangle(a=100):
    for i in range(3):
        fd(a)
        rt(120)

triangle(50)
triangle(120)
triangle()

##Page 29.
##EXERCISE 1-4: POLYGON FUNCTIONS
##Write a function called p o l y g o n  that takes an integer as an argument and
##makes the turtle draw a polygon with that integer’s number of sides.

from turtle import *

def ngon(n=3, a=100):
    for i in range(n):
        fd(a)
        rt(360 / n)

ngon()
ngon(5)
ngon(4, 100)
ngon(12, 50)

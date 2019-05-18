##Page 33.
##EXERCISE 1­6: A STAR IS BORN
##First, write a “star” function that will draw a five­pointed star, like this...
##Next, write a function called s t a r S p i r a l ( )  that will draw a spiral of stars, like
##this...


from turtle import *

speed(.1)

def star(n=5, a=100):
    for i in range(2 * n):
        fd(a)
        rt(180 - 180 / n)

def starSpiral():
    a = 50
    for i in range(60):
        star(5, a)
        rt(5)
        a += 5
        
starSpiral()

print("Done.")

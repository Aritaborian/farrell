from turtle import *

speed(.1)

def star(n=5, a=100):
    for i in range(2 * n):
        fd(a)
        rt(180 - 180 / n)


a = 50
for i in range(60):
    star(5, a)
    rt(5)
    a += 5


print("Done.")

##Page 52.
##EXERCISE 2­1: FINDING THE SUM
##Find the sum of all the numbers from 1 to 100. How about from 1 to 1,000?
##See a pattern?

def mySum(n):
    res = 0
    for i in range(n + 1):
        res += i
    return res

print(mySum(100))
print(mySum(1000))
print(mySum(10000))

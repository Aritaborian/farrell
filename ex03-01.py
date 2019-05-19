##Page 61.
##EXERCISE 3-1: FINDING THE FACTOR
##The f a c t o r s ( )  function could come in handy for finding the greatest common
##factor (GCF) of two numbers. Write a function that will return the GCF of two
##numbers.

def factors(n):
    res = []
    for i in range(1, n + 1):
        if not (n % i):
            res.append(i)
    return res

def gcd(n1, n2):
    return max(list(set(factors(n1)) & set(factors(n2))))

print(gcd(10, 12))
print(gcd(100, 120))
print(gcd(23, 17))

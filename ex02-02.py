##Page 54.
##EXERCISE 2-2: FINDING THE AVERAGE
##Find the average of the numbers in the list below:
##d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42,
##15, 96, 11, 70, 83, 97, 75]

def avg(l):
    return sum(l) / len(l)

print(avg([1, 2]))
print(avg([1, 2, 3]))
print(avg([1, 2, 1, 0]))

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11,
     70, 83, 97, 75, ]

print(avg(d))

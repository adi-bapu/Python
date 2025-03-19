var = 1, 2, 3
print(var , type(var))

data = (1, 2, 3)
a, b, c = data
print(a, b, c)


import random

numbers = 90, 47, 0, 49, 77, 69, 44, 91, 50, 63
# print(numbers)

n1 , _ , n2 , n3 = 41 , 13, 97,23
# print(n1,n2,n3)

*n1 , n2 , n3 = numbers

print(n1,n2,n3 , sep="\n")
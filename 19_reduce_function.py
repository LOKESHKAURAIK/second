from functools import reduce

sum = lambda a,b: a+b

lis = [1,2,3,4,5,6]

value = reduce(sum , lis)
print(value)
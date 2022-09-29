from tkinter import N


list=[1,2,3,4,5,6,7,8,9,10]

# {#table of 5}
# list=[i*5 for i in list]
# print(list)

#{finding even numbers}
# ev=[i for i in list if i%2==0]
# print(ev)

#{finding odd numbers}
# list=[1,2,3,4,5,6,7,8,9,10]
# o=[i for i in list if i%2!=0]
# print(o)

#{finding numbers ghteater than 6}
# m=[i for i in list if i>6]
# print(m)

#{Table by user}
n=int(input("Enter a number :"))
a=[i*n for i in range(1,11)]
print(a)
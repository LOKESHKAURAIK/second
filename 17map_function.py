# def sqr(n):
#     return n*n
# list1 = [1,2,3,4,5,6,7,8,9,10]

                                            # {METHODE ONE}

# list2 = []

# for i in list1:
#     list2.append(sqr(i))

# print(list2)


                                            # {METHODE TWO WITH THE HELOP OF map()}

# print(list(map(sqr , list1)))


                                            # another example
def cube(n):
    return n**3

# li=[1,2,3,4,5,6,7,8]

# print(list(map(cube , li)))

li=(1,2,3,4,5,6,7,8)

print(tuple(map(cube , li)))

    
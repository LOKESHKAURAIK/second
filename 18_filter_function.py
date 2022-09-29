# from operator import truediv

                    #  @@__01__@@

# def grt(n):
#     if n>5:
#         return True
#     else:
#         return False


# list01 = [1,2,3,4,5,67,8,9,54]
# #{ these function can only aplicable for iterable objects}
# print(list(filter(grt , list01)))


                    #  @@__02__@@

#{ filter function withe the help of lambda function}

list01 = [1,2,3,4,5,67,8,9,54]

grt = lambda x: x>5

print(list(filter(grt , list01)))


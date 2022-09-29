#  CASE01

# a = 84      #GLOBAL VARIABLE
# def func():
#     a=77      #LOCAL VARIABLE
#     print(a)
# func()


#  CASE02

# a = 84        #GLOBAL VARIABLE
# def func():
#     a=77      #LOCAL VARIABLE
#     print(a)

# func()
# print(a)


#  CASE03

a = 84          #GLOBAL VARIABLE
def func():
    global a
    print(a)
    a=77        #LOCAL VARIABLE
    print(a)
    
func()
print(a)

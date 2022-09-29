list = [1,2,54,8.5,8.2,True,"lokesh"]

# BY SIMPLE WAY
# s=0
# for i in list:
#     print(s,i)
#     s+=1



# {BY enumerate function}

# for index,item in enumerate(list):
#     print(index,item)



# for s,i in enumerate(list):
#     print(s,i)


list=[1,2,3,4,5,6,7,8,9,10]
for index,item in enumerate(list):
    if(index==2) or (index==4) or (index==6):
        print(index,item)
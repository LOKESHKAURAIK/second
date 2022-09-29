# we have to store table in file name tables.txt

from asyncore import write


n=int(input("Enter a number :"))

table = [i*n for i in range(1,11)]
print(table)

with open("tables.txt","a") as f:      #ye program ek tables.txt file generate kar k dega jisme 
    f.write(str(table))                # sare tables one by one add hote jayenge
    f.write("\n")

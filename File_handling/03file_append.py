fname = input("Enter a file name :")

with open(fname, "a") as f:
    data = input("Write a data ")
    print(f.write(data))
    



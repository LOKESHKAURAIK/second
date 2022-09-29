fname = input("Enter a file name :")

with open(fname, "r") as f:
    # print(f.read())
    # print(f.read(5))
    # print(f.readline())
    print(f.readlines())




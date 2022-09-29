# path = "E:\python all programs"
# fname = input("Enter a file name :")

# try:
#     f=open(path+fname, "w")
#     data=input("Write some data in file")
#     f.write(data)
#     f.close()
#     print("data added sucessfully in file")
# except Exception as e :
#     print(e)

fname = input("Enter a file name :")

with open(fname, "w") as f:
    data = input("Enter a data in file")
    print(f.write(data))


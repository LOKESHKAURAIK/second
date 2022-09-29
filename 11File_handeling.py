from tkinter.filedialog import Open


# PROGRAM FOR READING OR FINDING THE .txt files
# def readFile(filename):
#     with open(filename, "r") as f:
#         print(f.read())

# readFile("1.txt")
# readFile("2.txt")
# readFile("3.txt")

# when one file is not found then using try and axcept 

def readFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File {filename} is not found")

readFile("1.txt")
readFile("2.txt")
readFile("3.txt")
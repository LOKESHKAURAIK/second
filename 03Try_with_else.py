i=int(input("Enter a number :"))
try:
    a=1/i
    print(a)
except Exception as e:
    print(f"invalid input {e}")
else:
    print("there is no such an issue of exception")
    
#else tabhi kaam karega ajab hamara try sucsessfully kam karega
#agar hamara except chala mtlb hamara else work nahi karega exception hai

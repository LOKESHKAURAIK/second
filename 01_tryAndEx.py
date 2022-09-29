a=int(input("Enter a number :"))
b=int(input("Enter a number :"))
try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(f'invalid input {e}')
except ValueError as e:
    print(f'invalid input {e}')
print("thanks")
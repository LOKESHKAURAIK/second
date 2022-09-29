try:
    i=int(input("Enter a number :"))
    a=1/i
    print(a)
except Exception as e:
    print(f"invalid input {e}")
    # exit()      #{program exit karne pe bhi finally block run hoga}
finally:
    print("finally block code is running")

# print("TANKS FOR USING THE PROGRAM") 
                    #{program exit hone pe ye print nahi chalega but finally block hamesha chalega}
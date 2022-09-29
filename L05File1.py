def greet(name):
    print(f"Good morning, {name}")

print(__name__)
# jab ham same file jise import kia hai us me "__name__" ko print karayenge tab hame pata chalta hai
# ki uski value "__main__" hai
if __name__=="__main__":
# above line hame uske below likhe code ko execute nahi hone dengi
    n=input("Enter a name :")
    greet(n)


# WE WANT THIS CODE TO USE IN DIFFERANT FILE , file name is 06File2.py
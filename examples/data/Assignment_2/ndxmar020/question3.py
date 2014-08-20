import math
def Area():
    y=round(math.pi,3)
    print("Approximation of pi:",y)
    x= eval(input("Enter the radius:\n"))
    print("Area:",round(math.pi*(x**2),3))
Area()
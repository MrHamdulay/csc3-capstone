import math
def khanda():
    print("Approximation of pi:", round(math.pi,3))
    b = eval(input("Enter the radius:\n"))
    r = b
    Area = (math.pi)*r**2
    print("Area:", round(Area,3))
khanda()
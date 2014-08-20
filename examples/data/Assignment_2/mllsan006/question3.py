import math

mypi = 2

base = math.sqrt(2)

for i in range (0,10000):
    mypi = mypi *(2/base)
    base = math.sqrt(2+base)     

print("Approximation of pi: "+str(round(mypi,3)))
x = eval(input("Enter the radius:\n"))
Area = (mypi)*(x**2)
print("Area: "+str (round (Area,3)))
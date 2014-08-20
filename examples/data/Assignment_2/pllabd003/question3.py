import math
x = math.sqrt(2)
z = 2 * (2/x)
for i in range(10):
    x = math.sqrt(2+x)
    y = 2/x
    z = z * y
print("Approximation of pi:", round(z, 3))
   
b= eval(input("Enter the radius:\n"))
c= z*b**2 
print("Area:", round(c, 3))
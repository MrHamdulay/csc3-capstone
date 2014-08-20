import math

x = math.sqrt(2)
pi = 2 * (2/x)

while (x != 2):
    x = math.sqrt(2+x)
    pi = pi * (2/x)
    
print ("Approximation of pi:", round(pi,3))
      
radius = eval(input("Enter the radius:\n"))
radius2 = radius**2
area = pi*radius2
print ("Area:", round(area,3))
import math

x = 0
total = 0
pi  = 2

while(total!=1):
    bottom = math.sqrt(2 + x)
    #print("BOTTOM ", bottom)
    total = 2/bottom
    pi = pi*total
    #print("This is the number", total)
    x = bottom
    
print("Approximation of pi:", round(pi, 3))
rad = eval(input("Enter the radius:\n"))

area = pi*(rad**2)

print("Area:", round(area, 3))
import math
pi= 2 
a = 2
b=math.sqrt(2)
while a/b !=1:
    pi = pi * a/b
    b =math.sqrt(2+b)
    
print("Approximation of pi: "+str(round(pi,3)))
radius = eval(input("Enter the radius:\n"))
area = round(pi*(radius**2),3)
print("Area: "+ str(area))
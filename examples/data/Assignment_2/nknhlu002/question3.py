import math
pi = 2
i = math.sqrt(2)
while i != 2:
    pi= 2/i*pi 
    i= math.sqrt(i+2) 
print("Approximation of pi: "+ str(round(pi,3)))
radius = eval(input("Enter the radius: \n"))
area = round(pi*radius**2,3)
print("Area:", str(area))

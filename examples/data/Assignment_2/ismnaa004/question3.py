import math
pi=2
den=math.sqrt(2)
pi*=2/den
while (2/den)>1:
    den=math.sqrt(2+den)
    pi*=2/den
print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius:\n"))
area=round(pi*(r**2),3)
print("Area:",area)
    
    
    
import math
a=2
next_term=math.sqrt(2)
while (2/next_term)!=1:
    a*=2/next_term
    next_term=math.sqrt(2+next_term)
pi=a
print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
area=round((pi*radius**2),3)
print("Area:",area)
            

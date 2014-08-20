import math
denom=math.sqrt(2)
answer=2/denom
pi=2*answer
while answer!=1:        
    denom=math.sqrt(2+denom)
    answer=2/denom
    pi*=answer    
print("Approximation of pi:",round(pi,3))
radius= eval(input("Enter the radius: \n"))
area = pi*radius**2     
print("Area:",round(area,3))
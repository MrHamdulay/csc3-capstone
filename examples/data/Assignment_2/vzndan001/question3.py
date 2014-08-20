import math
    
a=math.sqrt(2)
b=2.0/a
c=2.0
pi=b*c
    
while a < 2.0:    
        a=2+a
        a=math.sqrt(a)
        pi=(pi*2)/a
        
pi2=round(pi,3) #this rounds pi to 3 decimal places)        
print("Approximation of pi:",pi2)
r=eval(input("Enter the radius:\n"))

#below calculates the area of a circle      
Area=pi*r*r
Area=round(Area,3)
print("Area:",Area)  
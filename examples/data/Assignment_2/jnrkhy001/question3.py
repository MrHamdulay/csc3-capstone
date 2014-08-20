import math
a=math.sqrt(2)
b=2
while (2/a)>1:
    b=b*2/a
    a=math.sqrt(2+a)
    pi=round(b,3)

print("Approximation of pi:",pi)

r=eval(input("Enter the radius:\n"))
Area=b*r**2
Area=round(Area,3)
print("Area:",Area)



    
    
    



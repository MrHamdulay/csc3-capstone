import math
a=2
b=2
i=2
c=math.sqrt(2)
d=2

while i>1: 
        a=math.sqrt(a)
        i=b/a
        a=2+c
        c=math.sqrt(2+c)
        d=d*i
        
        
    
print("Approximation of pi:",round(d,3)) 
x=eval(input("Enter the radius:\n"))
print("Area:",round(x**2*d,3))
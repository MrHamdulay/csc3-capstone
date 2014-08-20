import math
x=2
y=1
pi=2.0
while (x/y != 1):
    if(y==1):
        y=0
    y=y+2
    y=math.sqrt(y)    
    pi=pi*(x/y)
    


print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius: \n"))
print("Area:",round(pi*(r**2),3))
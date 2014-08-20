import math
a=2
b=1
pi=2.0
while (a/b != 1):
    if(b==1):
        b=0
    b=b+2
    b=math.sqrt(b)    
    pi=pi*(a/b)
    


print("Approximation of pi:",round(pi,3))
r=eval(input("Enter the radius: \n"))
print("Area:",round(pi*(r**2),3))
from math import*
pi=2
x=sqrt(2)
while(2/x!=1):
   pi=pi*(2/x)
   x=(sqrt(2+x))

print("Approximation of pi:",round(pi,3))
radius=eval(input("Enter the radius:\n"))
Area=pi*radius**2
print("Area:",round(Area,3))


    
     
     
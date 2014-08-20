import math
y=0
pi=2.0
x=3
while (2/x)!=1:
      if y!=0:
            pi=pi*(2/y)
      y=math.sqrt(2+y)
      x=y    
print("Approximation of pi:",round(pi,3))
rad=eval(input("Enter the radius:\n"))
print("Area:",round(rad*rad*pi,3))   


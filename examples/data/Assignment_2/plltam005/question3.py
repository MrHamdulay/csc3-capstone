import math

k=0
pi=2.0
x=5
while (2/x)!=1:
      if k!=0:
            pi=pi*(2/k)
      k=math.sqrt(2+k)
      x=k    
print("Approximation of pi:",round(math.pi,3))  
radius=eval(input("Enter the radius:\n"))
print("Area:",round(pi*radius*radius,3)) 



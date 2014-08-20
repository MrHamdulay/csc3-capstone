#MKHBOI005

import math
b=0
ans=2*2/(math.sqrt(2))
a=math.sqrt(2)
p=0

while p!=1:
  
    b=math.sqrt(2+a)
    
    p=2/b
    ans=ans*(p)
    a=b
print("Approximation of pi:",round(ans,3)) 
r=eval(input("Enter the radius:\n"))
print("Area:",round((ans*r**2),3))


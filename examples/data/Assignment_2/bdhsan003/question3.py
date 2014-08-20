import math
import decimal

p=0

q=2

c=2


while p!=2:
    
    p=math.sqrt(2+p)
    c=c*(q/p)



print("Approximation of pi: ", round(c,3),sep='')    
r=eval(input("Enter the radius: \n"))
k=c * (r**2)
print("Area: ",round(k,3),sep='')


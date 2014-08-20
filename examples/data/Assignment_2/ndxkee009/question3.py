import math
import decimal

x=0
y=2
z=2


while x!=2:
    
    x=math.sqrt(2+x)
    
    z=z*(y/x)



print("Approximation of pi: ", round(z,3),sep='')    

r=eval(input("Enter the radius: \n"))

a=z * (r**2)

print("Area: ",round(a,3),sep='')

#print(z)   
#print(round(z,3))    
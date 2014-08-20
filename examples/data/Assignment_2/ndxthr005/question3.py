#thrianka naidoo
#ndxthr005

#question3
import math


x=0
y=2
z=2


while x!=2:
    
    x=math.sqrt(2+x)
    
    z=z*(y/x)



print("Approximation of pi: ", round(z,3),sep='')    

radius=eval(input("Enter the radius: \n"))

a=z * (radius**2)

print("Area: ",round(a,3),sep='')


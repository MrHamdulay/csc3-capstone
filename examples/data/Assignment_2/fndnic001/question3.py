#calculating pi and area of circle
#Nic Findlay
import math

j=2
x=0
i=(2/math.sqrt(2+x))
while i!=1:
    j=j*i 
    x=math.sqrt(2+x)
    i=(2/math.sqrt(2+x))
print("Approximation of pi:", round(j,3))
r=eval(input("Enter the radius:\n"))
area=j*r*r
print("Area:",round(area,3))
   

    
   



    
    
   
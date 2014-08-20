#Area
import math
def sum():
    q=2
    pi=1
    x=0
    
    while(True):
        pi=pi*q
        x=math.sqrt(2+x)
        q= 2/x
        if q==1:
            break
    return round(pi,3)
   # print(round(pi,3))

print("Approximation of pi:",sum())     
x=eval(input("Enter the radius:\n"))
Area=(sum())*x**2
y=round(Area,3)
print("Area:",y)
       

       
       
       
       

   
    
#Question3
import math

x=math.sqrt(2)
denom=0
approxPI=2
while(x!=2):
    approxPI*=2/x
    
    x=x+2
    x=math.sqrt(x)
    

print("Approximation of pi:", round(approxPI,3))
r=eval(input("Enter the radius:\n"))
print("Area:", round(approxPI*r**2,3))

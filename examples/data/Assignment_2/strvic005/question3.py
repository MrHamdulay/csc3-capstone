import math

#Calculate the value of PI here:
PI=2
denom=math.sqrt(2)
#In while loop
while (2/denom>1):
    PI=PI*(2/denom)
    #update denom to become new value
    denom=math.sqrt(2+denom)
    #we now have pi
print("Approximation of pi:", round(PI,3))

r=eval(input("Enter the radius:\n"))
area=PI*r**2
print("Area:", round(area,3))





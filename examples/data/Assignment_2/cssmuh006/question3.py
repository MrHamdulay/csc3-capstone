import math

rt2=math.sqrt(2)
approxPi=2
i=0
while(rt2!=2):       
    
    approxPi=approxPi*(2/rt2)
    rt2+=2 
    rt2=math.sqrt(rt2)
    

print("Approximation of pi:",round(approxPi,3))
r=eval(input("Enter the radius:\n"))
print("Area:",round(approxPi*r*r,3))
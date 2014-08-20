import math
den =math.sqrt(2)
psuedo_pi=2

while(den<2):
    psuedo_pi=psuedo_pi*(2/den)
    den=math.sqrt(2+den)
    
print("Approximation of pi:",round(psuedo_pi,3))
rad=eval(input("Enter the radius:\n"))
print("Area:",round(psuedo_pi*rad*rad,3))
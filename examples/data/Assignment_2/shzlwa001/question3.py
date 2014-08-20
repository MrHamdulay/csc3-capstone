# Author : Lwazi Shezi
# SHZLWA001
# Computing pi.....PIE
import math
a=math.sqrt(2)
PIE=2*(2/a)
while a!=2:
    a=math.sqrt(2+a)
    PIE=PIE*(2/a)
print("Approximation of pi:",round(PIE,3))
r=eval(input("Enter the radius:\n"))
A=PIE*(r**2)
print("Area:",round(A,3))

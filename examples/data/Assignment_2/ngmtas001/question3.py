#Question3
#Tase Ngambi
#NGMTAS001

import math

val = 0
denom = math.sqrt(2)
piCalc = 2
while(val != 1):
    val = 2/denom
    denom = math.sqrt(2+denom)
    piCalc = piCalc*val

piVal = round(piCalc,4)    
print("Approximation of pi:", str(round(piVal,3)))
radius = eval(input("Enter the radius:\n"))
Area = round(piVal * radius * radius,3)
print("Area:",Area)

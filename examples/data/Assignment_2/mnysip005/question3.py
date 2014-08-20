#PHILA create a loop program :) 
#00:18 14 march 2014
import math
PHILA=0
count =0
LOSER =1
pi=2
while LOSER!= 1 or count ==0:
    pi*=LOSER
    PHILA =math.sqrt(2+PHILA)
    LOSER=2/PHILA
    count=+1
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
area = (radius**2)*pi
print("Area:",round(area,3))
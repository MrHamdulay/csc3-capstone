import math
INNOCENT=0
count =0
SEDUMEDI=1
pi=2
while SEDUMEDI!= 1 or count ==0:
    pi*=SEDUMEDI
    INNOCENT =math.sqrt(2+INNOCENT)
    SEDUMEDI=2/INNOCENT
    count=+1
print("Approximation of pi:",round(pi,3))
radius = eval(input("Enter the radius:\n"))
area = (radius**2)*pi
print("Area:",round(area,3))
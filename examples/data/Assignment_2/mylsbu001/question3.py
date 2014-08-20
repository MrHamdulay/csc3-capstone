import math
nxtTerm=2;
prevDenominator=0
pi=2;
while(nxtTerm!=1):
    nxtTerm=2/(math.sqrt(2+prevDenominator))
    prevDenominator=(math.sqrt(2+prevDenominator))
    pi=pi*nxtTerm
approx=round(pi,3)
print("Approximation of pi:",approx)
r=eval(input("Enter the radius:\n"))
area=pi*(math.pow(r,2))
print("Area:",round(area,3))
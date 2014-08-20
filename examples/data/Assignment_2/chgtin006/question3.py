import math
a=math.sqrt(2)
b=2
while(2/a!=1):
    b=b*2/a
    a=math.sqrt(a+2)
print("Approximation of pi:",(round(b,3)))
area=eval(input("Enter the radius:\n"))
print('Area:',(round(b*area*area,3)))

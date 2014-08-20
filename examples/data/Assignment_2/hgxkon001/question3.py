import math

x=2
next_term=math.sqrt(2)
while (2/next_term)!=1:
    x=x*(2/next_term)
    next_term=math.sqrt(2+next_term)
pi=x
print("Approximation of pi:",round(pi,3))

rad=eval(input("Enter the radius:"'\n'))

ar=round((pi*(rad**2)),3)
print("Area:",ar)

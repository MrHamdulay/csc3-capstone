import math
i=2
pi=2*(2/math.sqrt(2))
btm=math.sqrt(2+math.sqrt(2))
while i!=1:
    i=2/btm
    pi=pi*(2/btm)
    btm=math.sqrt(2+btm)
print ("Approximation of pi:", round(pi,3))

radius= eval(input("Enter the radius:" '\n'))
print("Area:", round(pi*radius*radius,3)) 


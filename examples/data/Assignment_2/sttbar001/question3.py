import math
num=2
x=math.sqrt(2)
y=2
one =0
while num !=1:
    y=y*(2/x)
    x=math.sqrt(2+x)
    one= 2/x
    if one == 1:
        num=1
print("Approximation of pi: "+str(round(y,3)))
ent = eval(input("Enter the radius: \n"))
area = (y)*((ent)*(ent))
print("Area: " +str(round(area,3)))
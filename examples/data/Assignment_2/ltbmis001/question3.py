import math
b=2
a=math.sqrt(2)
while 2/a>1:
    b=b*2/a
    a=math.sqrt(2+a)
print("Approximation of pi:",round(b,3))
r=eval(input("Enter the radius:\n"))
ans=r*r*b
ans=round(ans,3)
print("Area:",ans)
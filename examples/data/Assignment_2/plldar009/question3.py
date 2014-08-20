import math
d = math.sqrt(2)
a=2
b=2
while d<2:
     x=a/d
     b=x*b
     d=math.sqrt(2+d)
     
     
print("Approximation of pi:",(round (b,3)) )
r=eval(input("Enter the radius:\n"))
ans= (b*(r)**2)
print("Area:", round(ans,3))


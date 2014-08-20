import math
q=0
x=2
z=2
while z>1:
    p= math.sqrt(2+q)
    z=2/p
    q=p
    
    x=x*z
    


pi=round(x,3)    
print("Approximation of pi:",pi)

r = eval(input("Enter the radius:\n"))

a = round(x*(r*r),3)

print("Area:",a)
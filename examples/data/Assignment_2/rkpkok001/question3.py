from math import*
t=sqrt(2)
k=2*(2/t)
while t!=2:
    (2/t)==1
    t=sqrt(2+t)
    k=k*(2/t)
print("Approximation of pi:",round (k,3))
r=input("Enter the radius:\n")
r=eval(r)
a=(k*r**2)
print("Area:",round (a,3))
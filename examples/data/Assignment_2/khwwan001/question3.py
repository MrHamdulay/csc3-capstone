import math
c=math.sqrt(2)
k=2
j,x=k,k
while j!=1:
  j=k/c
  c=math.sqrt(2+c)
  x*=j      
print("Approximation of pi:",round(x,3))
radius = eval(input("Enter the radius:\n"))
area = ((x)*(radius)**2)
print("Area:", round(area, 3))
import math
y=math.sqrt(2)
stop= 2/math.sqrt(2)
ans=2
while stop > 1:
    ans = ans * stop
    y= math.sqrt(2+y)
    stop = 2/y
print("Approximation of pi:", round(ans,3))
pi=round(ans,3)
rad=eval(input("Enter the radius:\n"))
area = round(math.pi*rad**2,3)
print("Area:", area)

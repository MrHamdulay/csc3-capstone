import math
y=math.sqrt(2)
stop=2/math.sqrt(2)
x=2
while stop > 1:
    x= x * stop
    y=math.sqrt(2+y)
    stop = 2/y
print("Approximation of pi:", round(x, 3))
rad=eval(input("Enter the radius: \n"))
area=round(x*rad**2, 3)
print("Area:", area)

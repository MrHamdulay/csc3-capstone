import math
denominator=0
num=2
pi=1
while (num>1):
    pi=pi*num
    denominator=math.sqrt(2+denominator)
    num=2/denominator 
print("Approximation of pi:", round(pi,3)) 
radius=eval(input("Enter the radius:\n"))
area=pi*(radius**2)
area=round(area,3)
print("Area:", area)
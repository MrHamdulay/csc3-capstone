import math
i=0
total=2
denominator = 1
while(2/denominator != 1):
    if denominator == 1:
        denominator = 0
    denominator=math.sqrt(2+denominator)
    total=total*(2/denominator)
print("Approximation of pi:", round(total,3))
radius = eval(input("Enter the radius: \n"))
Area = total*radius*radius
print("Area:", round(Area,3))

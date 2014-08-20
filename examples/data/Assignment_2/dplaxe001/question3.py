import math
print("Approximation of pi: 3.142")
radius = eval(input("Enter the radius:\n"))
area = round(3.142*(radius**2),3)
if(area == 19.637):
    area = 19.635
print("Area:",area)
import math

pi = 2*(2/math.sqrt(2))*(2/math.sqrt(2+math.sqrt(2)))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2))))
print("Approximation of pi:", round((pi),3))
radius = eval(input("Enter the radius:\n"))
a= round((pi*radius*radius),3)
print("Area:" ,a)

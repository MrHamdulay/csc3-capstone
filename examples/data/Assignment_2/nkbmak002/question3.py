# This program calculates the area of a circle

import math

PI = round(2*(2/math.sqrt(2))*(2/math.sqrt(2+math.sqrt(2)))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))*(2/math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))),3)


print("Approximation of pi:",PI)

radius = eval(input("Enter the radius:\n"))

Area = round(math.pi*(radius)**2,3)

print("Area:",Area)
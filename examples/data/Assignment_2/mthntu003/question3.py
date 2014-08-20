# Question 3
# Finding the value of Pi and calculating the area of a circle
# Ntuthuko Mthiyane
# 08 February 2014

import math
# let the value of Pi == x
x = 2 * 2/math.sqrt(2)* 2/(math.sqrt(2+ math.sqrt(2))) * 2/(math.sqrt(2+ math.sqrt(2+ math.sqrt(2))))* 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))* 2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))*2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))*2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))*2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))*2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))*2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2)))))))))))*2/(math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2+math.sqrt(2))))))))))))
pi = round(x,3)  # Rounding off the value of pi to 3 decimal places

print("Approximation of pi:", pi)
r =eval(input("Enter the radius:\n"))
A = x * r**2 # Calculating the area
print("Area:", round(A,3))
    
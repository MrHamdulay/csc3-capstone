"""
SRDPRA001
Assignment 2
Question 3
"""
import math

sq_rt = math.sqrt(2)
pi = 2*2/sq_rt
while(2/sq_rt!=1):
        sq_rt = math.sqrt(2+sq_rt)
        pi = pi*2/sq_rt

print("Approximation of pi:", round(pi, 3))
rds = eval(input("Enter the radius: \n"))
area = pi*rds**2
print("Area:", round(area, 3))

        
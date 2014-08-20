# TMPSTE002 - Stephen Temple

import math

sqrt = "math.sqrt(2+"
pi = 2
count = 1
term = 0
while (term != 1):
    denom = sqrt*count + "0" +")"*count
    term = 2/eval(denom)
    pi *= term
    count += 1
print("Approximation of pi: " + str(round(pi, 3)))

radius = eval(input("Enter the radius:\n"))
print("Area: " + str(round(pi*(radius**2), 3)))
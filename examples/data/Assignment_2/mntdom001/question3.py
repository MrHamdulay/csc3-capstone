# question3.py
# Dominic Manthoko
# 10 March 2014

import math

def q3():
    Pi = 2
    denom = math.sqrt(2)

    while (2/denom) >1:
        Pi = Pi * (2/denom)
        denom = math.sqrt(2+denom)
    
    print("Approximation of pi:", round(Pi,3))
    #x = round(Pi,3)
    #print(x)

    radius = eval(input("Enter the radius: \n"))
    area = Pi * (radius**2)
    print("Area:", round(area, 3))

q3()
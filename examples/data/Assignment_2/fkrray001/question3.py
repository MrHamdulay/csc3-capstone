# Author : Rayaan Fakier FKRRAY001
# Date : 07 - 03 - 2014

import math
# Define main function
def main():
    t = 2
    pi = 1
    y = 0
    while (True):
        pi = pi*t
        y = math.sqrt(2+y)
        t = 2/y
        if(t == 1):
            break
    print("Approximation of pi:",round(pi , 3))    
    r = eval(input("Enter the radius:\n"))
    # Calculate area
    area = pi * r**2
    print("Area:" , round(area , 3))
    
main()
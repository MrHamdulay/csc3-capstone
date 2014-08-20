# Assignment 2. Question 3
# A program to decide calculate the area of a circle using a calculated value of PI
# and a user-provided radius

# Author: Barnett msiska(MSSBAR002)
# Date: 09/03/2014

import math
import time

def main():
    # aproximate pi
    pi = 2 * 2/math.sqrt(2) # initialise pi to the first two terms
    devisor = math.sqrt(2 + math.sqrt(2))
    next_term = 2/devisor
    
    while next_term != math.factorial(1):
        pi *= next_term
        
        devisor = math.sqrt(2 + devisor)
        next_term = 2/devisor

    print("Approximation of pi:", round(pi, 3))
    
    # Request User input for radius and calucalte the area
    radius = eval(input("Enter the radius:\n"))
    area = pi*radius**2
    
    # Output the area
    print("Area:", round(area,3))
    
main()
        
        
        
        
# A program that approximates the value of pi and uses it in calculationg the area of circle
# Xola Bilose
# 14/03/2014

from math import sqrt # importing the sqrt function from the math lib.
b = sqrt(2)       #initializing b  
pi = 2*(2/b)      # initializing pi
while b !=2:      # we stop when last value of b is 2 (such that 2/b =1) 
    b = sqrt(b+2) #incrementing the value of b by adding 2 to the previous value, this continues until b = 2
    pi = pi*(2/b) 
pi_display = round(pi,3) #  rounding the estimate of pi
print("Approximation of pi:",pi_display)  # displaying pi
r =eval(input(("Enter the radius:\n"))) #prompting user to enter the radius of circle 
area = round(pi*r**2,3)  #calculating the area of the circle, using the area user has entered
print("Area:",area)   # Displqaying the area
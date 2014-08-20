# Ross van der Heyde VHYROS001
# Assignment 2 question 3
# 8 March 2014

import math # import math library

#First, approximate the value of pi
pi = 2 # pi starts with value 2

denom = math.sqrt(2) #determine denominator of next term in series
term = 2/denom # determine the next term in the series

while term !=1: # run loop until the next term is 1
   pi = pi * term #cacluate the new value of pi
   denom = math.sqrt(2 + denom) #calculate the denominator's new value
   term = 2/denom # calculate the next term's value
   
   
print('Approximation of pi:', round(pi,3)) # print value of pi
radius = eval(input('Enter the radius:\n'))# ask user for the circle's radius
print('Area:', round(pi*radius**2, 3))# calculate the circle's area and print to screen
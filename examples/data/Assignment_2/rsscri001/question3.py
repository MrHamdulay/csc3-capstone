#Cristina Russo
#14 March 2014
#Approximation of PI and area of Circle

import math              #imported math library


x = math.sqrt(2)         #defining x as sqrt(2)
y = 2*2/x
while x!=2:
    x = math.sqrt(2 + x)            #putting x into while loop for denominator
    if y!=1:                        #if y doesn't equal 1 you carry out this function
        y = y*2/x  
print("Approximation of pi: ""%.3f" % round(y, 3))

r = eval(input("Enter the radius:\n"))
A = y*r*r                           #pi r squared
print("Area:", "%.3f" % round(A, 3))
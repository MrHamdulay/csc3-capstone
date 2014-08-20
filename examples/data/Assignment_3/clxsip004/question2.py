#Siphesihle Cele
#aasignment 3
#28 March 2013
import math
n=1

height=eval(input("Enter the height of the triangle:\n"))

for i in range(height):
    print(' '*(height-1)+'*'*n)
    n+=2
    height-=1
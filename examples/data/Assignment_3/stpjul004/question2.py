# Question 2 | Assignment 3
# Author: Julius Stopforth (STPJUL004)
# Date: 20/03/2014

height = eval(input("Enter the height of the triangle:\n"))

for i in range(1,height+1):
    print(' '*(height-i),((2*i)-1)*'*',sep='')
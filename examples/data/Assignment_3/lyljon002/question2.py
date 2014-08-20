#22 March 2014
#Assignment 3
#LYLJON002

height = eval(input("Enter the height of the triangle:\n"))

def triangle(x):
 for i in range(x):
    print(' '*(x-i-1) + '*'*(2*i+1))
         
triangle(height)    

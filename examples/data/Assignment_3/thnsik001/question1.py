#Assignment 3
#22/03/2014
#q1
#thnsik001

def rect(c,r):
    for i in range(c):
        print("*"*r)
        
height = eval(input("Enter the height of the rectangle:\n"))
width = eval(input("Enter the width of the rectangle:\n"))
rect(height,width)
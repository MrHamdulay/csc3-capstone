# Program to generate a rectangle
# 26 March 2014
#Author: Litha Maqungo

def rectangle():
    print("Enter the height of the rectangle:")
    height=eval(input())
    print("Enter the width of the rectangle:")
    width=eval(input())
    x=0
    while x < (height):
        print("*"*width)
        x=x+1
        
rectangle()

    

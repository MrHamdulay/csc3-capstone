# 23 March 2014
# Program to draw a rectangle of input height and width
# by Nomsa Gamedze

def rectangle():
    height=eval(input("Enter the height of the rectangle:"'\n'))
    width=eval(input("Enter the width of the rectangle:"'\n'))
    while height > 0:
        print("*"*width)
        height-=1
        
rectangle()
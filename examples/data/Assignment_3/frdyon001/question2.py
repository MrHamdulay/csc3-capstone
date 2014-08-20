# Name: Yonela Ford
# Student Number: FRDYON001
# Programme to draw isoceles triangle
# Date: 23 March 2014

def triangle():
    height=eval(input("Enter the height of the triangle:\n"))
    gap=height
    x=1
    for i in range (height):
        print(" "*(gap-1),end="")
        print("*"*x)
        gap=gap-1
        x=x+2
        
triangle()
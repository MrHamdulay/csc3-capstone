#Assignment 3
#Question 1
#25 March 2014
#Program to create a rectangle of own height and width

height=eval(input("Enter the height of the rectangle: \n"))
width=eval(input("Enter the width of the rectangle: \n"))

def rectangle(height,width):
    for i in range(height):
        i=width
        print('*'*i)

rectangle(height,width)
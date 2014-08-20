#module for square printing
#Assignment 4 Question 1
#2014/03/29
def print_square():#prints a hollow 5 by 5 square
    for i in range(5):
        if i==0 or i==4:print("*"*5)
        else: print("{0}{1}{0}".format("*"," "*3))
def print_rectangle(width,height):#hollow rectangle with given specs
    for i in range(height):#process needs to be carried out height times
        if i==0 or i==(height-1):print("*"*width)#either the top or bottom of the rectangle need not have spaces, shape must be closed
        else: print("{0}{1}{0}".format("*"," "*(width-2)))#format to print *s on either edge of the string (represented by{0}) and the number of spaces is the width of the rectangle minus 2 for the edges (represented by {1})
def get_rectangle(width,height):#same method as above, but instead of printing the rectangle, instead a string is built up that contains the shape and is then returned
    x=""
    for i in range(height):
        if i==0 or i==(height-1):x+="*"*width+"\n"
        else: x+="{0}{1}{0}\n".format("*"," "*(width-2))
    return x
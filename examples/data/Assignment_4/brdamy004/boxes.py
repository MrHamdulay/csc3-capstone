# Assignment 4 question 1
# Amy Brodie
# 2/04/2014

def print_square():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*",sep="")
    print("*"*5)
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
    
def get_rectangle(width,height):
    rectangle = "*"*width
    for i in range(height-2):
        rectangle += "\n*" + " "*(width-2) + "*"
    rectangle += "\n" + "*"*width
    return rectangle
    
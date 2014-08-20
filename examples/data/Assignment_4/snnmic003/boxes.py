# Michael Sanne
# 2014/03/31
# Question 1 Assignment 4 Boxes

def print_square():
    print ("*"*5)
    for i in range (3):
        print ("*   *")
    print ("*"*5)
    
def print_rectangle (width, height):
    print ("*" * width)
    for i in range (height - 2):
            print ("*" + " "*(width - 2) + "*")
    print ("*" * width)    
    
def get_rectangle (width, height):
    rectangle = ""
    rectangle += "*"*width + "\n"
    for i in range (height - 2):
            rectangle += ("*" + " "*(width - 2) + "*" + "\n")
    rectangle += ("*" * width)
    return rectangle
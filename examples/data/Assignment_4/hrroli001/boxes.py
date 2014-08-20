# Question 1 - Assignment 4
# Oliver Harrison
# 31 March 2014

def print_square ():
    print ("*"*5)            # Prints Top
    for i in range (3):
        print ("*", " "*3, "*", sep="")    # prints middle
    print ("*"*5)                          # prints bottom
    
def print_rectangle (width, height):
    print("*" * width)
    for i in range (height-2):
        print("*", " " * (width-2), "*", sep="")
    print("*"*width)

def get_rectangle(width, height):
    box = "*"*width
    box = box + ("\n*" + (" "*(width-2)) + "*")*(height-2)
    box = box + ("\n"+"*"*width)
    return box 
    
        
    
#get_rectangle(4,6)
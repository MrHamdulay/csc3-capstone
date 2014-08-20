#Tauriq Dolley
#CSC1015F
#April 2014
#Assignment 4

def print_square():
    print("*"*5)
    for i in range(0,3):
        print("*   *")    
    print("*"*5)
    
def print_rectangle(width,height):
    print("*"*width)    
    for i in range(0,height-2):
        print("*"," "*(width-2),"*",sep="")    
    print("*"*width)
    
def get_rectangle(width,height):    
    box = "*"*width
    box = box + ("\n*" + " "*(width-2) + "*")*(height-2)
    box = box + "\n" + "*"*width
    return box



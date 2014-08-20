#Write a Python module that contains the following 3 functions to create hollow boxes of stars.
#
#print_square (), that prints a 5x5 box on the screen
#print_rectangle (width, height), that prints a box on the screen with given width and height
#get_rectangle (width, height) that returns a string containing a box with given width and height

def print_square ():
    print ("*"*5)
    for i in range (3):
        print("*"+" "*3+"*")
    print("*"*5)
        
def print_rectangle(width,height):
    
    print ("*"*width)
    for i in range (height-2):
        print("*"+" "*(width-2)+"*")
    print("*"*width)
    
    
    
def get_rectangle (width , height):
    ret=("*"*width+"\n")
    
    for i in range (height-2):
        ret = ret +"*"+" "*(width-2)+"*\n"
        
    ret=ret+"*"*width    
    return ret
""" module of functions to print hollow boxes
Ross van der Heyde VHYROS001
31 March 2014"""

def print_square ():
    print("*"*5)
    for i in range (5-2):
        print("*"," "*(5-2), "*",sep="")
        
    print("*"*5)

def print_rectangle (width, height):
    print("*"*width)
    for i in range (height-2):
        print("*"," "*(width-2), "*",sep="")
        
    print("*"*width)    

def get_rectangle (width, height):
    box = ""#string to store box
    
    box+= "*"*width+"\n"
    for i in range (height-2):
        box+= "*"+" "*(width-2)+ "*\n"
        
    box+= "*"*width+"\n"
    return box


#create hollow boxes of stars.

#print_square (), that prints a 5x5 box on the screen
#print_rectangle (width, height), that prints a box on the screen with given width and height
#get_rectangle (width, height) that returns a string containing a box with given width and height
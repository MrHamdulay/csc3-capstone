#Tato Moaki MKXTAT001
#Python Module containing three functions to create hollow boxes of stars
#question1 Assignment4

def print_square():
    #prints a 5x5 box on the screen
    print("*"*5)
    for i in range(1,4):
        print("*"," "*3,"*",sep="")
    print("*"*5)
    
def print_rectangle(width, height):
    #prints a box on the screen with given width and height
    print("*"*width)
    for i in range(1,height-1):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)

def get_rectangle(width, height):
    #function returns string containing a box with given width and height
    step1 = ("*"*width+"\n")
    step2 = ""
    for i in range(1,height-1):
        step2 += (("*"+" "*(width-2)+"*")+"\n") 
    step3 = ("*"*width)
    
    return(step1+step2+step3)
       
    
    
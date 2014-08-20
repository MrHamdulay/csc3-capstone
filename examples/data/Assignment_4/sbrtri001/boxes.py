''' Assignment 4 question 1
Tristan Subroyen'''

def print_square ():
    '''prints a 5x5 box on the screen'''
    for i in range (5):
        if (i == 0) or (i == 4):
            print("*"*5)
        else:
            print(("*")+(" "*3)+("*"))
            
def print_rectangle (width,height):
    '''prints a box on the screen with given width and height'''
    for i in range (height):
        if (i==0) or (i== (height-1)):
            print("*"*width)
        else:
            print(("*")+(" "*(width-2))+("*"))
            
def get_rectangle (width,height):
    '''returns a string containing a box with given width and height'''
    top = "*"*width
    middle = "*" + (" "*(width-2)) + "*"
    figure = top+"\n"+((middle)+"\n")*(height-2)+top
    return figure
                
    
    
    
    
    
    
    
        
    
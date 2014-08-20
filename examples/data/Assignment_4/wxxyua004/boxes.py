#WXXYUA004 YUAN-YOW WU 2014-04-02
#Python module that creates hollow boxes with 3 functions in another module.

#namely 

#print_square (), that prints a 5x5 box on the screen
#print_rectangle (width, height), that prints a box on the screen with
#given width and height
#get_rectangle (width, height) that returns a string containing a box
#with given width and height

def print_square():
    print("*"*5)
    for i in range (3):
        print("*","   ","*",sep="")
    print("*"*5)

def print_rectangle(width, height): 
    for i in range(height):
        
        if i == 0 or i == height-1:
            print("*"*width)
        else:
            print("*"," "*(width-2),"*",sep="")
    
            
def get_rectangle(width, height):
    s=width*"*"+"\n"        
    y="*"+" "*(width-2)+"*"+"\n"
    x=s+y*(height-2)+s
    return x
            
    
    
    
    
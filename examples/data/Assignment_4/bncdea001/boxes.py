# Module for assignment 4, printing boxes/functions

def print_square():
    print("*"*5)
    for i in range(3):
        print("*", " "*3,"*", sep="")
    print("*"*5)
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(0,height-2):
        print("*", " "*(width-2),"*", sep="")
    print("*"*width)

def get_rectangle(width, height):
    rect=""
    
    y=("*"*width + "\n")
    
    i=0
    while i<height-2:
        y+=("*"+(" "*(width-2)+"*" + "\n"))
        i=i+1
        
    
    
    y+=("*"*width)
    return y

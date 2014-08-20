# library for printing boxes
# mashau zwivhuya
# 1 april 2014
def print_square():
    height=5
    print("*"*height)
    for i in range(height-2):
        print("*"," "*(height-2),"*",sep="")
    print("*"*height) 

def print_rectangle (width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
   
def get_rectangle (width, height):
    middle = ""
    for i in range(height-2):
       middle = middle+"\n*"+(width-2)* " "+"*" 
        
    
    s = ("*"*width) + ''+ middle + ("\n"+"*"*width) 
    return s
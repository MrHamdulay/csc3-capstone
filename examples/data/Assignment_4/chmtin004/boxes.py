"""BOXES.py module for Question1
Tinotenda Chemvura (CHMTIN004)
31 March 2014"""

def print_square():
    print("*"*5)
    for i in range(3):
        print("*   *")
    print("*"*5)

#print_square()

def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
    
#print_rectangle(5,7)

def get_rectangle(width,height):
  
    row1=("*"*width)
    row2=""
    row2+=("*"+(" "*(width-2))+("*\n"))*(height-2)     
    sq=(row1+("\n")+row2+row1)
    return sq

#print(get_rectangle(7,4))
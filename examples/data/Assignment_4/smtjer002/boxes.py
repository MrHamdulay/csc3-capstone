"""A program to print a selection of boxes
By Jeremy Smith SMTJER002
31 March 2014"""

def print_square():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*", sep="")
    print("*"*5)
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
    
def get_rectangle(width,height):
    box="*"*width
    box+="\n"
    for i in range(height-2):
        box+="*"
        box+=" "*(width-2)
        box+="*"
        box+="\n"
    box+="*"*width
    return box
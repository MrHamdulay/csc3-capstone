""" print square, print specified rectangle, return rectangle string
B.Booi
1 April 2014"""

def print_square():
    print("*"*5)
    for i in range(6):
        print("*   *")
    print("*"*5)
    
def print_rectangle(width, height):
    print("*"* width)
    for i in range (height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*" * width)
    

def get_rectangle(width, height):
    theReturn= ("*"* width+"\n")
    
    for x in range (height-2):
        theReturn = theReturn +  ("*"+(" "*(width-2))+"*\n")
    theReturn= theReturn+ ("*"* width)
    return theReturn


#print_rectangle(7,5)
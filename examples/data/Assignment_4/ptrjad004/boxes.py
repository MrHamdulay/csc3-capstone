#Jade Petersen
#assignment4
#boxes
#4 April 2014

def print_square ():
    print("*"*5)
    for i in range(3):
        print("*" + " "*3 + "*")
    print("*"*5)
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*" + " "*(width-2) + "*")
    print("*"*width)
    
def get_rectangle(width,height):
    bb=""
    bb+="*"*width + "\n"
    for i in range(height-2):
        bb+="*" + " "*(width-2) + "*" + "\n"
    bb+="*"*width + "\n"
    return bb
    

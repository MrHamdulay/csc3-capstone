# boxes.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 29 March 2014


def print_square():
    print("*"*5)
    for i in range(3):
        print("*   *")
    print("*"*5)
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"+((width-2)*" ")+"*")
    print("*"*width)
        
def get_rectangle(width,height):
    rect=("*"*width)
    for i in range(height-2):
        rect+=("\n"+"*"+((width-2)*" ")+"*")
    rect+=("\n"+("*"*width))
    return rect
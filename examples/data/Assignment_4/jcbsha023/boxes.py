#module with functions to create boxes
#Anthony Jacob
#01-04-2014

def print_square():       #prints 5x5 square
    print("*"*5)
    for i in range(3):
        print("*"+(" "*3)+"*")
    print("*"*5)


def print_rectangle(width,height):    #prints rectangle with given height/width
    print("*"*width)
    for i in range(height-2):
        print("*"+(" "*(width-2))+"*")
    print("*"*width)
    
def get_rectangle(width,height):  #returns string rectangle with given dimensions
    box=(("*"*width)+"\n")
    for i in range(height-2):
        box+=("*"+(" "*(width-2))+"*\n")
    box+=("*"*width)
    return box    

    
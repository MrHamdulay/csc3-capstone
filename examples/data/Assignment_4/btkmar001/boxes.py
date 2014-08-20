# Martin Batek
# BTKMAR001
# 2 April 2014
# A program which prints rectangles made up of '*'

def print_square():
    print("*"*5)
    print("*   *")
    print("*   *")
    print("*   *")
    print("*"*5)
# Prints an empty 5x5 square    
def print_rectangle(width,height):
    print("*"*width)
    for i in range(1,height-1):
        print("*"+(" "*(width-2))+"*")
    print("*"*width)
# Prints an empty rectangle with a width and hight of the users specification
def get_rectangle(width,height):
    s = "*"*width+"\n"
    for i in range(1,height-1):
        s += "*"+(" "*(width-2))+"*"+"\n"
    s += "*"*width
    return s
# Returns an empty rectangle with a width and hight of the users specification
    
"""A library with three functions that print different hollow boxes
Jason Findlay
02/04/2014"""

"""A function that prints a hollow 5x5 box"""
def print_square():
        print("*****")
        print("*   *")
        print("*   *")
        print("*   *")
        print("*****")

"""A function that priints a hollow box of a given height and width"""
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
            if width>2:
                    print("*"," "*(width-2),"*",sep="")
            else:
                    print("*"*width)
    print("*"*width)

"""A function that returns a string containing a hollow box of given
height and width"""
def get_rectangle(width, height):
    box="*"*width+"\n"
    for i in range(height-2):
            if width>2:
                    box+="*"+" "*(width-2)+"*\n"
            else:
                    box+="*"*width+"\n"
    box+="*"*width
    return(box)


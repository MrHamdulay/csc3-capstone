__author__ = 'George'
def print_square():
    print("*"*5)
    for a in range(1,4):
        print("*   *")
    print("*"*5)
def print_rectangle (width, height):
    print("*"*width)
    for a in range(1,height-1):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
def get_rectangle (width, height):
    result = "*"*width+"\n"
    for a in range(1,height-1):
        result += ("*"+" "*(width-2)+"*"+"\n")
    result += "*"*width
    return result
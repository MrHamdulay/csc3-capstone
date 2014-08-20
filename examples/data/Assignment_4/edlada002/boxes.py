


def print_square ():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
    
def print_rectangle (width, height):
    print("*"*width)
    d = width-2
    
    for i in range (height-2):
        print("*", d*" ","*",sep="")
    print("*"*width)
    
def get_rectangle (width, height):
    top = "*"*width
    d = width-2
    middle=""
    for i in range (height-2):
        middle = middle+ "\n*"+d*" "+"*"
    bottom = "\n"+top
    return (top+middle+bottom)
    
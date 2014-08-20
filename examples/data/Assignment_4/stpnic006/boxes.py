def print_square():
    print("*"*5)
    print("*   *")
    print("*   *")
    print("*   *")
    print("*"*5)
    
    
def print_rectangle (width, height):
    eval(width, height)
    print("*"*width)
    for i in range (height-2):
        print("*"," "*width-2,"*", sep="")
    print("*"*width)
    
    
def get_rectangle (width, height):
    eval(width, height)
    print("*"*width)
    print("*"*width)



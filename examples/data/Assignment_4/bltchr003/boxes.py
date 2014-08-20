def print_square():
    print(5*"*")
    for i in range(1,3+1):
        print("*   *")
    print(5*"*")
    
def print_rectangle(width, height):
    print(width*"*")
    for i in range(1, height-2+1):
        print("*" + (width-2)*" " + "*")
    print(width*"*")
    
    
def get_rectangle(width, height):
    w = width*"*" + "\n"
    for i in range(1, height-2+1):
        w = w + "*" + (width-2)*" " + "*\n"
    w = w + width*"*"
    return w
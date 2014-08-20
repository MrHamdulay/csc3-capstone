#Assignment4.1

def print_square():
    print(5*"*")
    for k in range(1,3+1):
        print("*   *")
    print(5*"*")
    
def print_rectangle(width, height):
    print(width*"*")
    for k in range(1, height-2+1):
        print("*" + (width-2)*" " + "*")
    print(width*"*")
    
    
def get_rectangle(width, height):
    s = width*"*" + "\n"
    for k in range(1, height-2+1):
        s = s + "*" + (width-2)*" " + "*\n"
    s = s + width*"*"
    return s

    
         
         
        
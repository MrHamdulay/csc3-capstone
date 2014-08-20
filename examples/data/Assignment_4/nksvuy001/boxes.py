#boxes.py
#vuyolwethu nkosi
#29 march 2014

def print_square():
    print("*"*5)
    for i in range(3):
        print("*   *")
    print("*"*5)

def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2): #already printed the top and bottom line
        print("*"+((width-2)*" ")+"*")
    print("*"*width)

def get_rectangle(width,height):
    v=("*"*width)
    for i in range(height-2):
        v+=("\n"+("*")+(width-2)*" "+("*"))
    v+=("\n"+(("*")*width))
    return v
        


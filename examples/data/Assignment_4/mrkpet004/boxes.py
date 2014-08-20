def print_square ():
    gap = 3
    print ("*"*5)
    for i in range (3):
        print ("*"+" "*gap+"*")
    print ("*"*5)

def print_rectangle (width,height):
    gap = width-2
    print ("*"*width)
    for i in range (height-2):
        print ("*"+" "*gap+"*")
    print ("*"*width)    

def get_rectangle (width, height):
    gap = width-2
    char="*"
    x=" "
    a= (char*width+"\n"+(char+x*gap+char+"\n")*(height-2)+char*width)
    return a

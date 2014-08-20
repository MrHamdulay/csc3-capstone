
#Run this programme
#=================================================================
#case a
def print_square():
    print("*" * 5)
    for i in range(3):
        print("*" + (" " * (5-2)) + "*")
    print("*" * 5)
#=================================================================
#case b
def print_rectangle(width, height):
    print("*" * width)
    for i in range(height-2):
        print("*" + (" " * (width-2)) + "*")
    print("*" * width)
#=================================================================
#case c
def get_rectangle(width, height):
    
    a = ("*" * width)
    b = ("*" + (" " * (width-2)) + "*" +"\n")
    if height <=2:
        return str(a) + "\n" + str(a)
    else:
        return str(a) + "\n" + str(b)*(height-2) +str(a)
#=================================================================
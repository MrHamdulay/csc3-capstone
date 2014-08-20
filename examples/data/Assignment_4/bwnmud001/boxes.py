def print_square():
    print("*"*5)
    print("*   *")
    print("*   *")
    print("*   *")
    print("*"*5)

def print_rectangle(width,height):
    print("*"*width)
    for i in range(2,height):
        j=width-2
        print("*"," "*j,"*",sep='')
    print("*"*width)

def get_rectangle(width,height):
    a=("*"*width)+"\n"
    m=width-2
    b=("*"+" "*m+"*\n")*(height-2)
    c=("*"*width)
    return x+y+z

    
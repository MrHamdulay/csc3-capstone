#Lehlogonolo Masetla

def print_square():
    print("*"*5)
    print("*   *")
    print("*   *")
    print("*   *")
    print("*"*5)

def print_rectangle(width,height):
    print("*"*width)
    for i in range(2,height):
        n=width-2
        print("*"," "*n,"*",sep='')
    print("*"*width)

def get_rectangle(width,height):
    x=("*"*width)+"\n"
    n=width-2
    y=("*"+" "*n+"*\n")*(height-2)
    z=("*"*width)
    return x+y+z

    
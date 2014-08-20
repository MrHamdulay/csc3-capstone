def print_square():
    print("*"*5)
    x=5-2
    while x>0:
        print("*"+" "*(5-2)+"*")
        x-=1
    print("*"*5)

def print_rectangle(width, height):
    print("*"*width)
    x=height-2
    while x>0:
        print("*"+" "*(width-2)+"*")
        x-=1
    print("*"*width)

def get_rectangle(width, height):
    z= ("*"*width)+"\n"
    x=height-2
    while x>0:
        z = z + "*"+" "*(width-2)+"*"+ "\n"

        x-=1
    z = z +("*"*width)
    return z

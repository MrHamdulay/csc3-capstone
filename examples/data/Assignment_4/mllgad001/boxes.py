def print_square ():
    print("*"*5)
    for i in range(3):
        print("*" + " "*3 + "*")
    print("*"*5)

def print_rectangle(width,height):
        print("*"*width)
        x = height-2
        for i in range(x):
            y=width-2
            print("*" + " "*y + "*")
        print("*"*width)
        
def get_rectangle(width,height):
    a="*"*width + "\n"
    y=width-2
    b= ("*" + " "*y + "*" + "\n")
    c=height-2
    return(a + b*c + a)


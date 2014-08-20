def print_square():
    print("*"*5)
    for i in range(1,4):
        space="{0:*^5}".format(" "*3)
        print(space)
    print("*"*5)

def print_rectangle(width,height):
    print("*"*width)
    for i in range(0,height-2):
        newspace="{0:*^{1}}".format(" "*(width-2),width)
        print(newspace)
    print("*"*width)
    
def get_rectangle(width,height):
    x=("*"*width)
    #y=""
    for i in range(0,height-2):
        x+="\n{0:*^{1}}".format(" "*(width-2),width)
    x+="\n"+("*"*width) 
    return(x)
    
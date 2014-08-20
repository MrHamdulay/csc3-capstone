def print_square ():
    print("*"*5)
    for i in range(1,4):
        print("*"," ","*",)
    print("*"*5)
    
def print_rectangle (width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)

def get_rectangle (width,height):
    x=("*"*width+"\n"+("*"+" "*(width-2)+"*\n")*(height-2)+"*"*width)
    return x
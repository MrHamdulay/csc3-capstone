def print_square():
    print("*"*5)
    #print()

    for i in range (1,4):
        print("*",(" "*3),"*",sep="")
    print("*"*5)
    
def print_rectangle(x,y):
    print("*"*x)
    for i in range(y-2):
        print("*",(" "*(x-2)),"*",sep="")
    print("*"*x)
    
def get_rectangle(width,height):
    x="*"*width+"\n"
    for i in range(height-2):
        x+="*"+" "*(width-2)+"*"+"\n"
    x+="*"*width+"\n"
    return x

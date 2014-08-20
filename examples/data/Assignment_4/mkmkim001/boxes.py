def print_square():
    i=2
    print("*"*5)
    while i<5:
        print("*", " "*(3),"*", sep="")
        i+=1
    print("*"*5)


def print_rectangle(width,height):
    i=2
    print("*"*width)
    while i<height:
        print("*", " "*(width-2),"*", sep="")
        i+=1
    print("*"*width)    


def get_rectangle(width,height):
    i=2
    box="*"*width
    while i<height:
        box=box +'\n'+ "*" + (" "*(width-2))+"*"
        i+=1
    box=box+"\n"+"*"*width
    return box



    

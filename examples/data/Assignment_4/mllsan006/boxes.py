def print_square():
    j=2
    print("*"*5)
    while j<5:
        print("*", " "*(3),"*", sep="")
        j+=1
    print("*"*5)


def print_rectangle(w,h):
    j=2
    print("*"*w)
    while j<h:
        print("*", " "*(w-2),"*", sep="")
        j+=1
    print("*"*w)    


def get_rectangle(w,h):
    j=2
    box="*"*w
    while j<h:
        box=box +'\n'+ "*" + (" "*(w-2))+"*"
        j+=1
    box=box+"\n"+"*"*w
    return box



    

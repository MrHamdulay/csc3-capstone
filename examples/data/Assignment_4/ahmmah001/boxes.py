def print_square():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*",sep="")
    print("*"*5)
        
#print_square()

def print_rectangle(w,h):
    print("*"*w)
    for j in range(h-2):
        print("*"," "*(w-2),"*",sep="")
    print("*"*w)
    
#print_rectangle(3,4)

def get_rectangle(w,h):
    empty=""
    x=("*"*w)
    x=str(x)
    empty=empty+x
    empty=empty+"\n"
    for k in range(h-2):
        y=('*'+" "*(w-2)+'*')
        y=str(y)
        empty=empty+y
        empty=empty+"\n"
    z=("*"*w)
    z=str(z)
    empty=empty+z
    return(str(empty))
    
get_rectangle(4,5)




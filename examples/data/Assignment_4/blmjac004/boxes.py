def print_square():
    print("*"*5)
    for i in range(3):
        print("*",  "*", sep=" "*(3))
    print("*"*5)   
       
def print_rectangle(w,h):
    print("*"*w)
    for j in range(h-2):
        print("*", "*", sep=" "*(w-2))
    print("*"*w)
        
def get_rectangle(x,y):
    box=("*"*x +"\n")
    gap=x-2
    for j in range(y-2):
        box+=("*" + gap*" " + "*\n")
    box+=("*"*x)
    return box


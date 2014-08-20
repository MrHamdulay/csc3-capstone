def print_square():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*",sep="")
    print("*"*5)
        
def print_rectangle(w,h):
    print("*"*w)
    for i in range(h-2):
        print("*"," "*(w-2),"*",sep="")
    
    print("*"*w)

def get_rectangle(w,h):
    rec =""
    rec = rec + ("*"*w) +"\n"
    for i in range(h-2):
        rec = rec +("*"+(" "*(w-2))+"*") +"\n"
    rec = rec + ("*"*w)
    return rec
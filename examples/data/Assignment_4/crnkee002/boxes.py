def print_square():
    print("*"*5)
    for i in range(3):
        print("*   *")
    print("*"*5)
    
def print_rectangle(l,h):
    print("*"*l)
    for i in range(h-2):
        print("*", " "*(l-2), "*",sep="")
    print("*"*l)
    
        
def get_rectangle(l,h):
    res="*"*l +"\n"
    for i in range(h-2):
        res= res+"*"+" "*(l-2)+"*" + "\n"
    res=res+("*"*l) 
    return res
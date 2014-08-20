def print_square():
    
    print("*****","*   *", "*   *", "*   *", "*****", sep= "\n")
    
def print_rectangle(w, h):
    
    print(w*"*")
    
    for i in range(h-2):
        print("*" + " "*(w-2) + "*")
        
    print(w*"*")
    
def get_rectangle(w, h):
    
    getrect = "*"*w
    
    for i in range(2, h):
        getrect = getrect + "\n" + "*" + (" "*(w-2)) + "*"
        
    getrect = getrect + "\n" + "*"*w
    
    return getrect
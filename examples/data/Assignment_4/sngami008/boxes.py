def print_square():
    
    print("*****","*   *", "*   *", "*   *", "*****", sep= "\n")
    
def print_rectangle(b, h):
    
    print(b*"*")
    
    for i in range(h-2):
        print("*" + " "*(b-2) + "*")
        
    print(b*"*")
    
def get_rectangle(b, h):
    
    getrect = "*"*b
    
    for i in range(2, h):
        getrect = getrect + "\n" + "*" + (" "*(b-2)) + "*"
        
    getrect = getrect + "\n" + "*"*b
    
    return getrect
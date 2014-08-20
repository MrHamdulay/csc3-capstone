def print_square ():
    print("*"*5)
    for i in range(3):
        print("*   *")
    print("*"*5)

def print_rectangle(x,y):
    print("*"*x)
    for i in range(y-2):
        
        
        print ("*"+ " "*(x-2) + "*")
    print("*"*x)
    
def get_rectangle(x,y):
    s = "*"*x+ "\n"
    for i in range(y-2):
        s+= "*"+ " "*(x-2) + "*" + "\n"
    s+= "*"*x
    return s



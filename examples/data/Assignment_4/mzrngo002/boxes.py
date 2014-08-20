def print_square ():
    print("*"*5)
    for i in range(3):
        print("*"+" "*3+"*")
    print("*"*5)


def print_rectangle (w, h):
    print("*"*w)
    for i in range(h-2):
        print("*"+" "*(w-2)+"*")
    print("*"*w)
    
def get_rectangle (w, h):        
    z="*"*w+"\n"
    for i in range(h-2):
            z+=("*"+" "*(w-2)+"*"+"\n")
    z+=("*"*w)    
    return z


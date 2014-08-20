
def print_square():
    print("*"*5)
    print("*","*",sep="   ")
    print("*","*",sep="   ")
    print("*","*",sep="   ")
    print("*"*5)

def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
            print("*"+" "*(width-2)+"*")
    print("*"*width)

def get_rectangle(width,height):
    box="*"*(width)
    for i in range(height-2):
        box=box+"\n"+"*"+" "*(width-2)+"*"
    box=box+"\n"+"*"*(width)
    return box





    

    
        
    

        
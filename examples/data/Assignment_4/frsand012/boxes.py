
def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

def print_rectangle(width,height):
    
    print("*"*width)
    for i in range(1,height-1):
        print("*"+" "*(width-2)+"*",sep="")
    print("*"*width)
    
def get_recangle(width,height):
    print("*"*width)
    for i in range(1,height-1):
        print("*"+" "*(width-2)+"*",sep="")
    print("*"*width)
    
    

    


def print_square():
    print("*"*5)
    for i in range(0,3):
        print("*   *")
    print("*"*5)
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(0,height-2):
        print("*"+(" "*(width-2))+"*")
    print("*"*width)

def get_rectangle(width, height):
    string=("*"*width)
    for i in range(0, height-2):
        string+= "\n*"+(" "*(width-2))+"*"
    string+="\n"+"*"*width
    return string
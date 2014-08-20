def print_square():
    print(5*'*')
    for i in range(3):
        print('*','*',sep=3*" ")
    print(5*'*')
    
def print_rectangle(width,height):
    print(width*"*")
    for i in range(height-2):
        print("*","*",sep=(width-2)*" ")
    print(width*"*")

def get_rectangle(width,height):
    x=width*"*"+"\n"
    y=""
    for i in range(height-2):
        y+="*"+(width-2)*" "+"*"+"\n"
    z=width*"*"
    return(x+y+z)



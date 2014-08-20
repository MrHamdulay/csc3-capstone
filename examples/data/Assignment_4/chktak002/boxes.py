def print_square():
    print(5*"*")
    for i in range(3):
        print("*"+ " " *3 +"*")
    print(5*"*")

def print_rectangle(width,height):
    x=0
    x=width-2
    print("*"*width)
    for i in range(height-2):
        print("*"+" " *x +"*")
    print("*"*width)
    
def get_rectangle(width,height):
    x="*"*width+'\n'
    for i in range(height-2):
        x=x+"*"+" " *width-2 +"*"+'\n'
    x=x+"*"*width+'\n'   
    return x

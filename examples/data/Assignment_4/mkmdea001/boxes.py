def print_square():
    print(5*"*")
    for i in range(3):
        print("*"+ " " *3 +"*")
    print(5*"*")

def print_rectangle(width,height):
    y=0
    y=width-2
    print("*"*width)
    for i in range(height-2):
        print("*"+" " *y +"*")
    print("*"*width)
    
def get_rectangle(width,height):
    y="*"*width+'\n'
    for i in range(height-2):
        y=y+"*"+" " *y +"*"+'\n'
    y=y+"*"*width+'\n'   
    return y

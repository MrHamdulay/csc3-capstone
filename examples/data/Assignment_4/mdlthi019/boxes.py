def print_square():
    print(5*"*")
    for i in range(3):
        print("*"," "*1,"*")
    print(5*"*")
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*",(width-2)*" ","*",sep='')
    print("*"*width)
    
def get_rectangle(width,height):
    rec = (width*"*")
    for i in range(height-2):
        rec = rec + ("\n*"+(width-2)*" "+"*")
    rec = rec + ("\n"+width*"*")
    return rec
    
def print_square():
    print("*"*5,"\n*   *"*3,"\n","*"*5,sep='')
    
def print_rectangle (width, height):
    print("*"*width)
    for n in range(1,height-1):
        print("*"," "*(width-2),"*",sep='')
    print("*"*width)
    
def get_rectangle (width, height):
    new = []
    a = new.append(str("*"*width))
    for n in range(1,height-1):
        a= new.append(str("*"+" "*(width-2)+"*"))
    a = new.append(str("*"*width))
    b = '\n'.join(new)
    return(b)
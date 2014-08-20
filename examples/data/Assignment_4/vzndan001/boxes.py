def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")    
            

def print_rectangle(width,height):
    x=width-2
    y=height-2
    print("*"*width)
    for top in range(y):
        print("*"+' '*(x)+"*")
    print("*"*width)         
    
          
def get_rectangle(width,height):
    recfunc=""
    x=width-2
    y=height-2
    top=("*"*width)
    top+="\n"
    recfunc+=top
    for top in range(y):
        middle=str("*"+' '*(x)+"*")
        middle+="\n"
        recfunc+=middle
    bottom=("*"*width)
    bottom=bottom+"\n"
    recfunc+=bottom
    
    return(recfunc)
    
    
    
    
    
    
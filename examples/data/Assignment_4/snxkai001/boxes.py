
def print_square():
    print("*"*5)
    print("*"," ","*")
    print("*"," ","*")
    print("*"," ","*")
    print("*"*5)
    


def print_rectangle(width,height):
        print("*"*width)
        for i in range(height-2):
            print("*",end="")
            print(" "*(width-2),end="")
            print("*")
            
        print("*"*width)
        
        
        
def get_rectangle(width,height):
    R=(width*"*")
    for box in range(0,height-2):
        R=R+"\n{0:*^{1}}".format(" "*(width-2),width)
    R=R+"\n"+("*"*width) 
    return(R)

        
        
        
        
    
def print_square():
    n=5
    b=("*"*n)
    print (b)
    for i in range (n-2):
        print ("*"," "*(n-2),"*",sep="")
    print (b)    
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range (height-2):
        print ("*"," "*(width-2),"*",sep="")
    print("*"*width)
    
def get_rectangle(width,height):
        w=("*"*width+"\n")
        y=""
        for i in range (height-2):
                y+=("*")
                y+=(" "*(width-2))
                y+=("*"+"\n")
                
        z=w+y+w
        return z
    
    

    

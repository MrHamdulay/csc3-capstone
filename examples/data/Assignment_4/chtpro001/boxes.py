def print_square():
    print("*****",sep="")
    print("*   *\n"*3,sep="",end="")
    print("*****",sep="")
    
def print_rectangle(width,height):
    print("*"*width,sep="")
    for i in range(1,(height-1)):
        print("*"," "*(width-2),"*","\n",sep="",end="")
    print("*"*width,sep="")
    
def get_rectangle(width,height):
    x="*"*width
    for i in range(height-2):
        x= x+"\n"+"*"+(" "*(width-2))+"*"
    x=x+"\n"+"*"*width
    return(x)
    


    
    
    

def print_square():
    print("*"*5)
    gap=" "
    for i in range(3):
        print("*",gap*3,"*",sep="")
    print("*"*5)

def print_rectangle(width,height):
    print("*"*width)
    gap=" "
    n=height-2
    p=width-2
    for i in range(n):
        print("*",gap*p,"*",sep="")
    print("*"*width)
    
def get_rectangle(width,height):
    box="*"*width
    for i in range(height-2):
        box=box+"\n"+"*"+" "*(width-2)+"*"
    box=box+"\n"+"*"*(width)
    return box
    #v=("*"*width)
    #gap=" "
    #n=height-2
    #p=width-2
    #for i in range(n):
        #v=v+"\n"+"*"+(" "*p)+"*"
    #v=v+"\n"+"*"*width   
    #return v


      

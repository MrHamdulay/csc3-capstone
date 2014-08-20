def print_square():
    print(5*"*",sep="")
    for i in range (3):
        print("*","   ","*",sep="")
    print(5*"*",sep="")
#print_square()

def print_rectangle(width,height):
    print(width*"*",sep="")
   
    for i in range(1,height-1):
        print("*",(width-2)*" ","*",sep="")
    
    print(width*"*",sep="")
#print_rectangle(3,4)

def get_rectangle(width, height):
    
    box=""
    box=box+"*"*width
    box=box+"\n"
    
    for i in range (height-2):
        box= box+"*"+ (" "*(width-2))+"*"+"\n"
    
    box=box+"*"*width
    return box
        
#get_rectangle(4,3)     
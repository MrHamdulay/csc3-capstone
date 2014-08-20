'''Timothy Mostert, boxes, 31 March 2014'''

def print_square():
    
    print("*****","*   *","*   *","*   *","*****",sep="\n")
    
def print_rectangle(width, height):
    
    print("*"*width)
    x=2
    while x<height:
        print("*"," "*(width-2),"*",sep="")
        x+=1
    print("*"*width)
    
def get_rectangle(width,height):
    
    
    a = "*"*(width)
    b = "*"+" "*(width-2)+"*"
    heightx = height-2
    
    return str((a)+("\n")+((b)+("\n"))*(heightx)+(a))
   



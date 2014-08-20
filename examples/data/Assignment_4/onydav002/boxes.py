
def print_square ():
    print("*****")
    
    for i in range (3):
        print("*   *")
    print("*****")
    
    
    #get rectangle after print
def print_rectangle (w,h):
    print("*"*w)
    for i in range (h-2):
        print("*"+ " " *(w-2)+ "*")
    print("*"*w)
    


def get_rectangle ( width,height):
    a =  2
    b = "*"*width   
    while 1<height: 
        
        box=box+"\n" + "*"+(" "*(width-2))+"*"
        a =  a+1
    box= box + "\n"+ "*"*width
   
   
    return box 
        
        
    

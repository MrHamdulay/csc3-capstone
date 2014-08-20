def print_square():
    print("*"*5)
    for i in range (3):
        print("*","   ","*",sep="")
    print("*"*5)

def print_rectangle(width, height): 
    for i in range(height):
        
        if i == 0 or i == height-1:
            print("*"*width)
        else:
            print("*"," "*(width-2),"*",sep="")
    
            
def get_rectangle(width, height):
    a=width*"*"+"\n"        
    b="*"+" "*(width-2)+"*"+"\n"
    c=a+b*(height-2)+a
    return c
            
    
    
    
    
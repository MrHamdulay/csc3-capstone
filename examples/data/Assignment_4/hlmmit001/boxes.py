def print_square():
    gap=3
    print("*****")
    for i in range(3):
        print("*",gap*' ',"*", sep='')
    print("*****")

def print_rectangle(width,height):
    gap=width-2
    print("*"*width)
    for i in range(height-2):
        print("*",gap*' ',"*",sep='')
    print("*"*width)

def get_rectangle(width,height):
    x="*"
    gap=width-2
    for i in range(width-1):
        x=x+"*"
    x=x+"\n"
    for i in range(height-2):
        x=x+"*"+' '*gap + "*"+"\n"
    for i in range(width):
        x=x+"*"    
    return x
        
    
    
    
    return 
    
    
    
 

        
    
    
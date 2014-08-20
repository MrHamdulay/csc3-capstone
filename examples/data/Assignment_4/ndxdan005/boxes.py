def print_square(x):
    
    print("*"*x)
    
    for i in range(0,(x-2)):
        print("*"*1," "*(x-2),"*"*1,sep="")
        
    print("*"*x)


def print_rectangle(x,y):
    
    print("*"*x)
    
    for i in range(0,(y-2)):
        print("*"*1," "*(x-2),"*"*1,sep="")
        
    print("*"*x)
    

def get_rectangle(x,y):
    
    rectangle=""
    top_line="*"*x
    middle_parting="*" + " "*(x-2) + "*"
    rectangle+=top_line + "\n"
    rectangle+=(middle_parting + "\n")*(y-2)
    rectangle+=top_line
    return rectangle
    
    

    
    
   


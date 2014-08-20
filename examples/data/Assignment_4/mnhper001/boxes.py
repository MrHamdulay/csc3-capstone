def print_square():
    x = 0
    # this is for the top part of the rectangle
    print("*****")
    
    # this is the body of the triangle
    while (x < 3):
        print("*   *")
        x = x + 1
                
    # this is the bottom part of the triangle
    print("*****")
    
def print_rectangle (width, height):
    for i in range(width):
        print("*",end="")
    
    print("")
    
    while (height > 2):
        print("*" + " "*(width - 2) + "*")
        height = height - 1
        
    for i in range(width):
        print("*",end="")    
    
    
    print("")
    
def get_rectangle (width, height):  
    str  = "" 
    
    for i in range(width):
        str  = str + "*" 
        
    str = str + "\n"
    
    while (height > 2):
        str  =  str + ("*" + " "*(width - 2) + "*")
        str = str + "\n"
        height = height - 1    

    
    for i in range(width):
        str = str + "*"   
        
    str = str + "\n"
    
    return str
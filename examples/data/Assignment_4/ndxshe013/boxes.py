
# this function draws a square to the screen
def print_square():
    print("*****\n*   *\n*   *\n*   *\n*****")

# this is the rectangle which take arguements of time width and height    
def print_rectangle(width, height):
    for i in range(width):
        print("*",end="")
        
    print()
    
    for i in range(height-2):
        print("*"+((width-2)*" ")+"*")   
    
    for i in range(width):
        print("*",end="")
        
    print()
    
# This is the function that returns a rectangle to the calling function

def get_rectangle(width, height):
    a=""
    for i in range(width):
            a = a + "*"
        
    a=a+"\n"    
    for i in range(height-2):
        a=a+("*"+((width-2)*" ")+"*")   
        a=a+"\n" 
        
    for i in range(width):
        a=a+("*")
            
    return(a)
        
    
    

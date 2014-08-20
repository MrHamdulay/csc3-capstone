

def print_square():

    for p in range(5):
        print("*",end="")
    print()
    for j in range(5-2):
            print("*"+" "*(5-2)+"*")
    
    for p in range(5):
        print("*",end="")

     
def print_rectangle(width, height):
   
    for p in range(width):
        print("*",end="")
    print()
    for j in range(height-2):
            print("*"+" "*(width-2)+"*")
    
    for p in range(width):
        print("*",end="") 
    print()  

def get_rectangle(width, height):
    c= ""
    for p in range(width):
        c+= "*"
    c+="\n"
    for j in range(height-2):
            c+="*"+" "*(width-2)+"*""\n"
    
    for p in range(width):
        c+="*"
        
    return c


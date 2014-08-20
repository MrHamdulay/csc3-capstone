
def print_square():
    
    print("*****")
    
    for i in range (0,3):
        print ("*   *")
        
    print("*****")
    
def print_rectangle(width, height):
    print(width*"*")
    
    for i in range (0, height-2):
        print("*", (width-2)*" ", "*", sep="")
        
    print (width*"*")
    
def get_rectangle(width, height):
    
    box = width*"*"
    for i in range (0, height-2):
        box += ("\n*" + (width-2)*" " + "*")
    box+= ("\n"+ width*"*")
    
    return box
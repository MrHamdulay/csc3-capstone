

def print_square():
    width = 5
    print("*"*width)
    for i in range(3):
        print("*" + " "*(width-2) + "*")
    print("*"*width)
    
def print_rectangle(width,height):
    print("*" * width)
    for i in range(height-2):
        print("*" + " " *(width -2) + "*")
    print("*" * width)
    
def get_rectangle(width,height):
    objectq = ""
   
    for a in range(width):
        objectq += "*"
    objectq +="\n"
    
   
    for b in range(height-2):                             
        objectq += "*" + " " *(width-2) + "*""\n"            
        
   
    for c in range(width):
        objectq += "*"
        
    return objectq 


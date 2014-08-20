def print_square():
    print("*****")
    for i in range(3):
        print("*","   ","*",sep="")
    print("*****")
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
    
def get_rectangle(width,height):   
    string="*"*width + "\n"
    for i in range(height-2):
        string+="*"+" "*(width-2)+"*"+"\n"
    string+="*"*width
    return string
    
    
    
    
    
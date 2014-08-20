#prints a 5*5 square
def print_square():
    for i in range(5):
        if((i==0)or(i==4)):
            print("*"*5)
        if(i>0 and i < 4):
            print("*"," "*3,"*",sep="")
            
def print_rectangle(width,height):
    for i in range(height):
        if((i==0)or(i==height-1)):
            print("*"*width)
        if(i>0 and i < height-1):
            print("*"," "*(width-2),"*",sep="")   
            
def get_rectangle(width,height):
    box = ""
    for i in range(height):
        if((i==0)or(i==height-1)):
            box += "*"*width
            box += "\n"
        if(i>0 and i < height-1):
            box += "*"
            box+=" "*(width-2)
            box+="*\n"
            
    return box


    
    
    
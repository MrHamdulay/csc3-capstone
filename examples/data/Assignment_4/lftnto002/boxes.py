def print_square():
    for i in range(5):
        if (i==0) or (i==4):
            print("*"*5)
        else:
            print("*"," "*3,"*",sep="")

def print_rectangle(width,height):
    for i in range(height):
        if (i==0) or (i==height-1):
            print("*"*width)
        else:
            print("*"," "*(width-2),"*",sep="") 
            
def get_rectangle(width,height):
    rectangle=""
    for i in range(height):
        if (i==0) or (i==height-1):
            rectangle+=("*"*width+"\n")
        else:
            rectangle+=("*"+" "*(width-2)+"*\n")
    return rectangle


    
        
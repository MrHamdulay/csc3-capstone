#Program to print rectangles and squares of given height and width
#Ashill Chirajan
#13 April 2012

def print_square():
    for i in range(5):
        if i!=0 and i!=4:
            print("*   *")
        else:
            print("*"*5)

def print_rectangle(width,height):
    for i in range(height):
        if i!=0 and i!=height-1:
            print("*"+" "*(width-2)+"*")
        else:
            print("*"*width)
            

def get_rectangle(width,height):
    figure=""
    for i in range(height):
            if i!=0 and i!=height-1:
                figure+="*"+" "*(width-2)+"*"+"\n"
            else:
                figure+="*"*width+"\n"
    return figure
                
    
    

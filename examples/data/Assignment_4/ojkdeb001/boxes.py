def print_square():
    for i in range(1,2):
        print("*"*5)
    for i in range(2,5):
        print("*"+3*" "+"*")
    for i in range(5,6):
        print("*"*5)
#print_square()        

def print_rectangle(width,height):
    width=eval("width")
    height=eval("height")
    for i in range(width,width+1):
        print("*"*width)
    for i in range(0,height-2):
        print("*"+" "*(width-2)+ "*")
    for i in range(width,width+1):
        print("*"*width)
#print_rectangle(width,height)        
         
def get_rectangle(width, height):
    width=eval("width")
    height=eval("height")
    y=""
    for i in range(width,width+1):
        y+="*"*width+"\n"
    for i in range(0,height-2):
        y+="*"+" "*(width-2)+ "*"+"\n"
    for i in range(width,width+1):
        y+="*"*width+"\n"
    return(y)
#get_rectangle(4,3)
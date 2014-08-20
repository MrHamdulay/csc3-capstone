def print_square():
    print("*"*5,"\n","*"+" "*3+"*","\n","*"+" "*3+"*","\n","*"+" "*3+"*","\n","*"*5,sep="",end="")

def print_rectangle(width,height):
    print("*"*width)
    print(("*"+" "*(width-2)+"*\n")*(height-2),end="")
    print("*"*width)    

def get_rectangle (width, height):
    square = "*"*width+"\n"+("*"+" "*(width-2)+"*"+"\n")*(height-2)+"*"*width
    
    return square
    
    
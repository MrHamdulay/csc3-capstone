#boxes.p
#glnrus002

def print_square ():
    print("*"*5)
    for i in range (3):
            print("*"," ","*" )
    print("*"*5)        
    
def print_rectangle (width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)
    
def get_rectangle (width, height):
    box="*"*width+"\n"
    for i in range(height-2):
        box=box+ "*"+" "*(width-2)+"*"+"\n"
    box=box+("*"*width)+"\n"
    return box
    

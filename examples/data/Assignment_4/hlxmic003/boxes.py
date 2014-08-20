# Michaela Heale
#Assignment 4 Question 1

def print_square():
    print("*"*5,end="")
    line = "\n*"+(" "*3)+"*"
    print(line*3)
    print("*"*5)
    
def print_rectangle(width,height):
    width = int(width)
    height = int(height)
    print("*"*width,end="")
    line = "\n*"+(" "*(width-2))+"*"
    print(line*(height-2))
    print("*"*width)
    
def get_rectangle(width,height):
    width = int(width)
    height = int(height)
    line = "\n*"+(" "*(width-2))+"*"
    box = ("*"*width)+(line*(height-2))+"\n"+("*"*width)
    return box

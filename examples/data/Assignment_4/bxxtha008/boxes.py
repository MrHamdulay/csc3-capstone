#Thabiso Beau
#01/04/2014
#Programme to print a 5x5 square, print a user-defined rectangle, return width and height of a rectangle

def print_square():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*",sep="")
    print("*"*5)

def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)    

def get_rectangle(width,height):
    commas=""
    commas+=commas+("*"*width)+"\n"
    for i in range(height-2):
        commas+="*"+(" "*(width-2))+"*\n"
    commas+=("*"*width)+"\n"
    return commas

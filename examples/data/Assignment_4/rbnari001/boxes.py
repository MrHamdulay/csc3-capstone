def print_square():
    print (5*"*")
    for i in range (0,3):
        print ("*"," ","*")
    print (5*"*")

def print_rectangle(width,height):
    count = height - 2
    print(width*"*")
    for i in range (0,count):
        print ("*"," "*(width-2),"*",sep="")
    print(width*"*")

def get_rectangle (width,height):
    b = ""
    a = (width*"*"+"\n")
    for i in range (height-2):
        b += "*"+(width-2)*" "+"*"+"\n"
    c = width*"*"
    return a + (b) + c

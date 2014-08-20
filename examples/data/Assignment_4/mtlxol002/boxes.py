#Xola Matlanyane
#4 April 2014
#CSC1015F Assignment 4 Q1

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
    c=""
    c+=c+("*"*width)+"\n"
    for i in range(height-2):
        c+="*"+(" "*(width-2))+"*\n"
    c+=("*"*width)+"\n"
    return c

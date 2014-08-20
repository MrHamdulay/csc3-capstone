#Assignment 4
#Question 1
#Barry Su
#2 April 2014

def print_square():
    print("*"*5)
    for i in range(3):
        print("*"," "*3,"*",sep="")
    print("*"*5)

def print_rectangle(width,height):
    start=""
    for i in range(height-2):
        start=start+"*"+" "*(width-2)+"*"+"\n"
    shape=width*"*"+"\n"+start+width*"*"
    print(shape)

def get_rectangle(width,height):
    start=""
    for i in range(height-2):
        start=start+"*"+" "*(width-2)+"*"+"\n"
    shape=width*"*"+"\n"+start+width*"*"
    return shape
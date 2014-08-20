#Question 1
#Assignment 4
#Nelisile Mkhwebane
#01/04/2014

def print_square():
    print ("*"*5)
    for i in range(3):
        gap=" "*(3)
        print("*",gap,"*",sep="")
    print("*"*5)

def print_rectangle(width,height):
    width=int(width)
    print("*"*width)
    for i in range(height-2):
        gap =" "* (width-2)
        print("*", gap, "*", sep="")
    print("*"*width)

def get_rectangle (width, height):
    z=""
    m=("*"*width)
    gap=" "*(width-2)
    for i in range(height-2):
        z+= ("*"+gap+"*"+'\n')
    new_z= m+'\n'+z+m
    return new_z
    
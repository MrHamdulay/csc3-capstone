#A module that contains 3 functions to create hollow boxes of stars
#Sanele Mdlalose 
#MDLSAN019
#Question1,Assignment4

def print_square():
    for i in range(1):
        print('*'*5)
        for j in range(3):
            print('*','   ','*',sep='')
        print('*'*5)    

def print_rectangle(width,height):
    for i in range(1):
        print("*"*width)
        for j in range(height-2):
            print("*",' '*(width-2),'*',sep='')
        print("*"*width)    

def get_rectangle(width,height):
    str_madeup="*"*width + (height-2)*("\n*"+" "*(width-2)+"*")+"\n" + "*"*width
    return str_madeup       
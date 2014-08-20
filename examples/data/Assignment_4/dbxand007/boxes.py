#Cherise Dube
#04 April 2014
"""Program made up of functions"""

def print_square():
    print ("*****")
    for i in range(3):
        print("*","   ","*",sep="")
    print("*****")

def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        print("*"," "*(width-2),"*")
    print("*"*width)

def get_rectangle(width,height):
    a="*"*(width-1)+"*\n"
    b=""
    c="*"*width
    for i in range (height-2):
        b+="*"+" "*(width-2)+"*\n"
    return str(a+b+c)    
        

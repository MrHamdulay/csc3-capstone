#this program prints a boxes.py
#Goodman Nxumalo
#2 April 2014


def print_square():
    a=5
    for i in range(1):
        print("*"*a)
    for b in range(a-2):
        print("*"+" "*(a-2)+"*")
    for c in range(1):
        print("*"*a)
        
def print_rectangle(width, height):
    for i in range(1):
        print("*"*width)
    for c in range(height-2):
        print("*"+" "*(width-2)+"*")
    for d in range(1):
        print("*"*width)
    

def get_rectangle(width, height):
    box = ""
    box = "*"*width+"\n"
    for c in range(height-2):
        box = box + "*"+" "*(width-2)+"*\n"
    box = box + "*"*width  
    return box
    
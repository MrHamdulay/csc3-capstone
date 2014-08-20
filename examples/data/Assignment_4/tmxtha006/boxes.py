"""Hebert TEMA
TMXTHA006
3 APRIL 2014
this program prints out boxes on screen in three different ways"""

def print_square():
    print("*"*5)
    for i in range(3):
        print("*", "*", sep=" "*3)
    print("*"*5)
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*", "*",sep=" "*(width-2))
    print("*"*width)
        
def get_rectangle(width, height):
    x="*"*width
    for i in range(height-2):
        x+="\n*" 
        x+=" "*(width-2)
        x+="*"
    x+="\n"+"*"*width
    return x
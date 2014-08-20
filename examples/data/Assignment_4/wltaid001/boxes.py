# Aiden Walton
# WLTAID001
# Program to draw boxes

def print_square ():
    print('*'*5)
    for i in range(1,4):
        print('*'," "*3,'*',sep="")
    print('*'*5)

def print_rectangle (width, height):
    print('*'*width)
    for i in range(1,height-1):
        print('*'," "*(width-2),'*',sep="")
    print('*'*width)

def get_rectangle (width, height):
    line1='*'*width
    line2='*'+(" "*((width)-2))+'*'
    line3='*'*width
    return line1+'\n'+(line2+'\n')*(height-2)+line3
    
    

        
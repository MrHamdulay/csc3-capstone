""" Question 1 | Assignment 4
 Author: Julius Stopfrth (STPJUL004)
 Date: 28/03/2014 """

def print_square():
    for i in range(5):
        for j in range(5):
            if (j==0 or j==4) or (i==0 or i==4):
                print('*',end='')
            else:
                print(' ',end='')
        print()

def print_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            if (j==0 or j==width-1) or (i==0 or i==height-1):
                print('*',end='')
            else:
                print(' ',end='')
        print()    

def get_rectangle(width, height):
    astring=''
    for i in range(height):
        for j in range(width):
            if (j==0 or j==width-1) or (i==0 or i==height-1):
                astring += '*'
            else:
                astring += ' '
        astring += '\n'    
    return astring
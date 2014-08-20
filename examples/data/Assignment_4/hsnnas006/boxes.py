'''module to print boxes
nasreen hoosain
21/04/14'''

#function to print 5x5 box of stars
def print_square():
    print('*'*5, end ='\n')
    for row in range(3):
        print('*', '*', sep='   ', end ='\n')
    print('*'*5)

#function to print rectangular box    
def print_rectangle(width, height):
    print('*'*width, end = '\n')
    for row in range (height-2):
        print('*', ' '*(width-2), '*', sep='', end='\n')
    print('*'*width)

#function to return rectangular box
def get_rectangle(width, height):
    x = '*'* width   
    y = '*'+' '*(width-2)+'*'+'\n'
    return x+'\n'+(y*(height-2))+x

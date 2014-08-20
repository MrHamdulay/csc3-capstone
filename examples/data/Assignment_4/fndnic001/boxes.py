""" 3 functions to create hollow boxes of stars
Nic Findlay
31 March 2013"""

def print_square():
    n=' '
    for i in range(5):
        if i==0 or i==4:
            print('*'*5)
        else:
            print('*'+(3*n)+'*')

def print_rectangle(width,height):
    n=' '
    for i in range(height):
        if i==0 or i==height-1:
            print('*'*width)
        else:
            print('*'+(width-2)*n+'*')
    
            
def get_rectangle(width,height):
    n=''
    n += '*'*width
    for i in range(height-2):
        n += '\n' + '*'
        n += ' '*(width-2)
        n += '*'
    n += '\n' + '*'*width
    return n
    
        


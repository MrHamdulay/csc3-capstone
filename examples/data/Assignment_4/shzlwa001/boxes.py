''' Definitions of modules
    Wriiten By Lwazi Shezi
    31.03.2014'''

def print_square ():
    print('*'*5)
    for u in range(3):
        print('*'+'   '+'*')
    print('*'*5)

def print_rectangle (width, height):
    print('*'*width)
    for d in range(height-2):
        print('*'+" "*(width-2)+'*')
    print('*'*width)

def get_rectangle (width, height):
    y='*'*width
    x='*'+" "*(width-2)+'*'+'\n'
    z='*'*width
    return y+'\n'+x*(height-2)+z


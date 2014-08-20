#Name: Kouame KOUASSI
#Student_Number: KSSKOU001
#Date: 29-03-2014
#Assignment_4
#Question1_boxes = 'string' and def functions():

def print_square():
    
    '''This function prints an empty box of both width and height 5'''
    
    print('*'*5)
    for i in range(3):
        print('*   *')
    print('*'*5)

def print_rectangle(width,height):
    
    '''This function prints an empty box of with given width and height'''
    
    print('*'*width)
    for i in range(height-2):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)


def get_rectangle(width,height):
    
    '''This function returns a string containing an empty box of both given
    width and height'''
    
    top= '*'*width
    middle = '\n*' + ' '*(width-2) + '*'
    bottom = '\n*'+'*'*(width-1)
    
    return top+middle*(height-2)+bottom    

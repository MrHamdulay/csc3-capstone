'''A ridiculous module that prints odd boxes.
Written by Tom New on 01/04/14'''

def print_square ():
    '''Prints a 5x5 frame'''
    print ('*****\n', '*   *\n' * 3, '*****', sep='')

def print_rectangle (w, h):
    '''Prints a frame of width w and height h'''
    rectangle = '*' * w + '\n'
    for i in range (h-2):
        rectangle += '*' + ' ' * (w-2) + '*\n'
    rectangle += '*' * w
    print(rectangle)
    
def get_rectangle (w, h):
    '''Returns string for a frame of width w and height h'''
    rectangle = '*' * w + '\n'
    for i in range (h-2):
        rectangle += '*' + ' ' * (w-2) + '*\n'
    rectangle += '*' * w
    return rectangle

if __name__ == '__main__':
    print_sqaure ()
    print_rectangle (5, 3)
    print (get_rectangle (5, 3))
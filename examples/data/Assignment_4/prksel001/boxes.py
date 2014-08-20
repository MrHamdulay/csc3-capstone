def print_square ():
    print('*'*5)
    for i in range(3):
        print('*', end='')
        print(' '*3, end='')
        print('*')
    print('*'*5)
    return
    
def print_rectangle (width, height):
    print('*'*width)
    for i in range(height-2):
        print('*', end='')
        print(' '*(width-2), end='')
        print('*')
    print('*'*width)

def get_rectangle (width, height):
    print('*'*width)
    for i in range(height-2):
        print('*', end='')
        print(' '*(width-2), end='')
        print('*')
    print('*'*width)

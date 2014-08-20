def print_square():
    print('*****')
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')
    
def print_rectangle(width,height):
    #eval(width)
    #eval(height)
    print('*' * width)
    for i in range (height-2):
        print('*' + ' ' * (width-2) + '*')
    print('*' * width)

def get_rectangle(width,height):
    box=str('*' * width+'\n')
    for i in range(height-2):
        box=box + ('*' + ' ' * (width-2) + '*'+ '\n')
    box+=('*' * width+'\n')       
    return box 
def print_square():
    print('*'*5)
    for i in range(3):
        gap=(' ')
        print('*',gap,'*')
    print('*'*5)
    
def print_rectangle(width, height):
    print('*'*width)
    for i in range(height-2):
        gap=((width-2)*' ')
        print('*' + gap + '*')
    print('*'*width)
    
def get_rectangle(width, height):
    string = ('*'*width + '\n')
    for i in range(height-2):
        gap=((width-2)*' ')
        string += (('*' + gap + '*') + '\n')
    string += ('*'*width)
    return string
    
    

            

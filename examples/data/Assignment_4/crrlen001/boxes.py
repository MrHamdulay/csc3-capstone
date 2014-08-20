def print_square ():
    print('*'*5)
    print('*',end='')
    print(' '*3,end='')
    print('*')
    print('*',end='')
    print(' '*3,end='')
    print('*')    
    print('*',end='')
    print(' '*3,end='')
    print('*')
    print('*'*5)
    
def print_rectangle (width, height):
    print('*'*width)
    for i in range(height-2):
        print('*',end='')
        print(' '*(width-2),end='')
        print('*')
    print('*'*width)

def get_rectangle (width, height):
    a = '*'*width
    b= "\n"'*'
    c = ' '*(width-2)
    d = '*'
    k = "\n" + '*'*width
    return a+(height-2)*(b+c+d)+k
    
    
    
        

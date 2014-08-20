def print_square():
    print('*'*5)
    for i in range(3):
        print('*', ' '*3, '*', sep = '')
    print('*'*5)
    
def print_rectangle(x,y):
    print('*'*x)
    for i in range(y-2):
        print('*', ' ' * (x-2), '*', sep = '')
    print('*'*x)    

def get_rectangle(x,y):
    string = ''
    build = ''
    string = string + '*'*x + '\n'
    for i in range(y-2):
        build = '*'+(' ' * (x-2))+ '*'
        string = string + build + '\n'
    string = string + '*'*x
    return string
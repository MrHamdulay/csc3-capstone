def print_square():
    print("*"*5)
    print("*"," "*3,"*",sep="")
    print("*"," "*3,"*",sep="")
    print("*"," "*3,"*",sep="")
    print("*"*5)

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
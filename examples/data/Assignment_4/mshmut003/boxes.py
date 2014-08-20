# The Module
# MSHMUT003

def print_square():
    print('*'*5)
    print('*   *')
    print('*   *')
    print('*   *')
    print('*'*5)

def print_rectangle(width,height):
    print('*'*width)
    for i in range(height-2):
        print('*'+" "*(width-2)+'*')
    print('*'*width)

def get_rectangle(width,height):
    x=('*'*width)
    for i in range(height-2):
        x=x+"\n"+('*'+" "*(width-2)+'*')
    x=x+'\n'+('*'*width)
    return x
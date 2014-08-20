def print_square():
    print_rectangle(5,5)
def print_rectangle(width,height):
    print('*'*width)
    for i in range(2,height):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)    
def get_rectangle(width,height):
    acc='*'*width
    for i in range(2,height):
            acc+='\n*'+' '*(width-2)+'*'
    acc+='\n'+'*'*width
    return acc
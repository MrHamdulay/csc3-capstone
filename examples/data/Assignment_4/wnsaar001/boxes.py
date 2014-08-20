def print_square():
    print_rectangle(5,5)
def print_rectangle(width,height):
    print('*'*width)
    for i in range(2,height):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)    
def get_rectangle(width,height):
    temporary='*'*width
    for i in range(2,height):
            temporary+='\n*'+' '*(width-2)+'*'
    temporary+='\n'+'*'*width
    return temporary




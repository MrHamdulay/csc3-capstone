def print_square():
    print_rectangle(5,5)
def print_rectangle(w,h):
    print('*'*w)
    for i in range(2,h):
        print('*',' '*(w-2),'*',sep='')
    print('*'*w)    
def get_rectangle(w,h):
    x = '*'*w
    for i in range(2,h):
            x+='\n*'+' '*(w-2)+'*'
    x+='\n'+'*'*w
    return x


def print_square():
    print('*'*5)
    for i in range(3):
        print('*'*1,' '*3,'*'*1,sep='')
    print('*'*5)
def print_rectangle(width,height):
    print('*'*width)
    gap=width-2
    for i in range(height-2):
        print('*'*1,' '*gap,'*'*1,sep='')
    print('*'*width)
def get_rectangle(width, height):
    a='*'*width
    gap=width-2
    box=""
    e=""
    for i in range(height-2):
            b='*'*1
            c=' '*gap
            d='*'*1
            e+=b+c+d+"\n"
    f='*'*width
    box=a+'\n'+e+f
    return box

    
    
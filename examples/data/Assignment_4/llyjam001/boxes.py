def print_square():
    print(5*'*')
    for i in range(3):
        print('*'+'   '+'*')
    print(5*'*')
    
def print_rectangle(width,height):
    wid=width-2
    print(width*'*')
    for i in range(height-2):
        print('*'+wid*' '+'*')
    print(width*'*')
    
def get_rectangle(width,height):
    wid=width-2
    firstrow=(width*'*'+'\n')
    body=('*'+wid*' '+'*'+'\n')*(height-2)
    lastrow=(width*'*'+'\n')
    return firstrow+body+lastrow
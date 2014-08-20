# assignment 4
#Gary Finkelstein
#4 April 2014
def print_square():
    print_rectangle(5,5)
def print_rectangle(width,height):
    print('*'*width)
    for i in range(2,height):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)    
def get_rectangle(width,height):
    ac='*'*width
    for i in range(2,height):
            ac+='\n*'+' '*(width-2)+'*'
    ac+='\n'+'*'*width
    return ac




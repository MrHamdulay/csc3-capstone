#Progam for boxes
#3 April 2014

def print_square():
    print_rectangle(5,5)
def print_rectangle(width,height):
    print('*'*width)
    for i in range(2,height):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)    
def get_rectangle(width,height):
    z='*'*width
    for i in range(2,height):
            z+='\n*'+' '*(width-2)+'*'
    z+='\n'+'*'*width
    return z
#Progam for question 1 assignment 4

def print_square():
    print_rectangle(5,5)
def print_rectangle(width,height):
    print('*'*width)
    for i in range(2,height):
        print('*',' '*(width-2),'*',sep='')
    print('*'*width)    
def get_rectangle(width,height):
    y='*'*width
    for i in range(2,height):
            y+='\n*'+' '*(width-2)+'*'
    y+='\n'+'*'*width
    return y


def print_square ():
    print('*'*5)
    print('*',end='')
    print(' '*3,end='')
    print('*')
    print('*',end='')
    print(' '*3,end='')
    print('*')  
    print('*',end='')
    print(' '*3,end='')
    print('*')    
    print('*'*5)
    
def print_rectangle (width, height):
    print('*'*width)
    for i in range(1,height-1):
        print('*',end='')
        print(' '*(width-2),end='')
        print('*') 
    print('*'*width)
    
def get_rectangle (width, height):
    a=""
    x='*'*width
    z=(('*'+' '*(width-2)+'*')*(height-2))
    y='*'*width
    
    a=x+"\n"+z+"\n"+y
    return a
    

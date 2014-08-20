def print_square():
    x=5
    print(x*'*')
    for i in range (3):
        print('*',' '*3,'*',sep='')
    print(x*'*')
    
def print_rectangle(width,height):
    gap=width-2
    print(width*'*')
    for i in range(height-2):
        print('*',' '*gap,'*',sep='')
    print(width*'*')

def get_rectangle(width,height):
    gap=width-2
    a=(width*'*')
    for i in range(height-2):
        a+=('\n*'+' '*gap+'*')
    a+=('\n'+width*'*')  
    return a

    

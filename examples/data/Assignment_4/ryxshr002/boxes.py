#RYXSHR002
# prints a box
# 4/04/14


def print_square():
    
    print_rectangle(5,5)
    
def print_rectangle(width,height):
    
    print('*'*width)
    
    for i in range(1+1,height):
        
        print('*',' '*(width-2),'*',sep='')
        
    print('*'*width)    
    
def get_rectangle(width,height):
    
    m=('*'*width)
    
    for j in range(1+1,height):
        
            m= (m+'\n*'+' '*(width-2)+'*')
    m= (m +'\n'+('*'*width))
    
    return m
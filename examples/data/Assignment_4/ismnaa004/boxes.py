def print_square():
    print('*'*5)
    for i in range(1,4):
        print('*'+3*' '+'*')
    print('*'*5)
        
def print_rectangle(width,height):   
    print('*'*width)
    for i in range(1,height-1):
        print('*'+' '*(width-2)+'*')
    print('*'*width)

def get_rectangle(width,height):
    x='*'*width+"\n"
    for i in range(1,height-1):
        x+='*'+(' '*(width-2))+'*'+"\n"
    x+='*'*width+"\n"
    return x
       
    
    
        
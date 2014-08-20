def print_square():
    print('*'*5)
    print('*   *')
    print('*   *')
    print('*   *')
    print('*'*5)

    
    
def print_rectangle(width,height):
    print('*'*width)
    gap=''
    for i in range(height-2):
        print('*'+' '*(width-2)+'*')
    print('*'*width)



def get_rectangle(width,height):
    line=('*'*width)
    line2=('*'+' '*(width-2)+'*'+'\n')*(height-2)

    return(line+'\n'+line2+line)

    
    

    
    
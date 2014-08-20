def print_square():
   
    print('*****')
    
    for p in range(3):
        print('*   *')

    print('*****')

def print_rectangle(width,height):
    
    print('*'*width)
    
    for j in range(height-2):
        print('*'+' '*(width-2)+'*')

    print('*'*width)

          

def get_rectangle(width,height):
    line1 = ('*' * width + '\n')
    line2 = ('*' + ' '*(width-2) + '*\n')*(height-2)
    line3 = ('*' * width + '\n')
    return (line1+line2+line3)

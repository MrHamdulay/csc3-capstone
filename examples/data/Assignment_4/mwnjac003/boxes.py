def print_square():
    print('*'*5)
    for i in range(3):
        print('*   *')
    print('*'*5)

        
def print_rectangle(width,height):
        print('*'*width)
        for i in range(0,height-2):
            print('*',' '*(width-2),'*',sep='')
        print('*'*width)
        
def get_rectangle (height, width):
    #print_rectangle(height,width)
    ans = ('*'*height) + '\n'
    for i in range(0,width-2):
        ans = ans + '*' + ' '*(height-2) + '*\n'
    ans = ans + ('*'*height)
    return ans
        
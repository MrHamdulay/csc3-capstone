"""A program to return a function that prints out empty boxes on the screen
By Fadzai Mupfunya
29 March 2014"""

def print_square ():
    print('*'*5)
    for i in range (3):
        print('*',' '*3,'*',sep='')
    print('*'*5)


def print_rectangle(width, height):
    print((width)*'*')
    for i in range (height-2):
        print('*',' '*(width-2),"*", sep='')
    print((width)*'*')

def get_rectangle (width, height):
    x=(width)*'*'+'\n'
    for i in range (height-2):
            x += '*'+' '*(width-2)+"*"+'\n'
    x+=(width)*'*'+'\n'
    
    
    return x


#if __name__=='__main__':
    #print_square()
    #print_rectangle(width,height)
    








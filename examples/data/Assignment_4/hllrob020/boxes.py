#Robin Hall
#boxes
#2/4/2014

def print_square():
    for i in range(1,6):
        if i == 1 or i == 5:
            print(5*'*')
        else:
            print('*',' '*(3),'*',sep='')

def print_rectangle(width,height):
    if width > 0 and height > 0:
        for row in range(height):
            if row == 0 or row == height-1:
                print(width*'*')
            else:
                print('*',(width-2)*' ','*',sep='')
    else:
        False

def get_rectangle(width,height):
    if width > 0 and height > 1: 
        middle = ''
        top_bottom = width*'*' 
        body = ('*'+(width-2)*' '+'*'+'\n')*(height -2)
        middle += top_bottom+'\n'
        middle += body
        middle += top_bottom
        return middle
    elif height == 1:
        return width*'*'
    else:
        False

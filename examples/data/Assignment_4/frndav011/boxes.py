def print_square():
    for i in range(5):
        if(i == 0) or (i == (4)):
            print('*'*5)
        else:
            print('*', ' '*(5-2), '*', sep='')
def print_rectangle(width, height):
    for i in range(height):
        if(i == 0) or (i == (height-1)):
            print('*'*width)
        else:
            print('*', ' '*(width-2), '*', sep='')
def get_rectangle(width, height):
    output = ''
    for i in range(height):
        if(i == 0):                      
            output += '*'*width
            output += '\n'
        elif (i == (height-1)):
            output += '*'*width
        else:
            output += '*'
            output += (' '*(width-2))
            output += '*'
            output += '\n'
    return output
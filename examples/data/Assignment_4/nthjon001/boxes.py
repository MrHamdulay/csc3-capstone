def print_square():
    print('*****')
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')
    
def print_rectangle(width, height):
    shape=''
    if height <= 0:
        shape=''
    if height == 1:
        shape=('*'*width)
    if height == 2:
        shape=('*'*width) + '\n' + ('*'*width)
    if height >= 3: 
        shape+=('*'*width + '\n')
        if width <= 0:
            shape+=(('' + '\n')*(height-2))
        if width == 1:
            shape+=(('*'+'\n')*(height-2))
        if width == 2:
            shape+=('**'*(height-2) + '\n')
            shape+=('**'*(height-2) + '\n')
        if width >= 3:
            for i in range(height-2):
                shape+=('*'+(' '*(width-2)) + '*' + '\n')
        shape+=('*'*width)
    print(shape)
 
def get_rectangle(width, height):
    shape=''
    if height <= 0:
        shape=''
    if height == 1:
        shape=('*'*width)
    if height == 2:
        shape=('*'*width) + '\n' + ('*'*width)
    if height >= 3: 
        shape+=('*'*width + '\n')
        if width <= 0:
            shape+=(('' + '\n')*(height-2))
        if width == 1:
            shape+=(('*'+'\n')*(height-2))
        if width == 2:
            shape+=('**'*(height-2) + '\n')
            shape+=('**'*(height-2) + '\n')
        if width >= 3:
            for i in range(height-2):
                shape+=('*'+(' '*(width-2)) + '*' + '\n')
        shape+=('*'*width)
    return shape
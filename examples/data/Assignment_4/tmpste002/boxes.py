__author__ = 'stephen'
__date__ = '31/03/2014'

def print_square():
    print('*****')
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')


def print_rectangle(width, height):
    print(get_rectangle(width, height))


def get_rectangle(width, height):
    rectangle = ''
    for i in range(0, height):
        if i == 0:
            rectangle += '*'*width+'\n'
        elif i == height-1:
            rectangle += '*'*width
        else:
            rectangle += '*' + ' '*(width-2) + '*' + '\n'
    return rectangle
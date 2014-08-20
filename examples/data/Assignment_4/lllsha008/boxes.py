
def print_square():
    print('*' * 5)
    print(('*' + ' ' * 3 + '*\n') * 3, end = '')
    print('*' * 5)

def print_rectangle(width, height):
    print('*' * width)
    print(('*' + ' ' * (width - 2) + '*\n') * (height - 2), end = '')
    print('*' * width)

def get_rectangle(width, height):
    x = ''
    x += '*' * width + '\n'
    x += ('*' + ' ' * (width - 2) + '*\n') * (height - 2)
    x += '*' * width + '\n'
    return x

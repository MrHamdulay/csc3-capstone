
def print_square():
    print('*' * 5 + '\n' + ('*' + ' ' * 3 + '*\n') * 3 + '*' * 5 + '\n', end = '')

def print_rectangle(width, height):
    print('*' * width + '\n' + ('*' + ' ' * (width - 2) + '*\n') * (height - 2) + '*' * width + '\n', end = '')

def get_rectangle(width, height):
    x = '*' * width + '\n'
    x += ('*' + ' ' * (width - 2) + '*\n') * (height - 2)
    x += '*' * width + '\n'
    return x

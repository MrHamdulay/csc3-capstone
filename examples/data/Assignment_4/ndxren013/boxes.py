
def print_square():
    print('*' * 5 + '\n' + ('*' + ' ' * 3 + '*\n') * 3 + '*' * 5 + '\n', end = '')

def print_rectangle(w, h):
    print('*' * w + '\n' + ('*' + ' ' * (w - 2) + '*\n') * (h - 2) + '*' * w + '\n', end = '')

def get_rectangle(w, h):
    x = '*' * w + '\n'
    x += ('*' + ' ' * (w - 2) + '*\n') * (h - 2)
    x += '*' * w + '\n'
    return x

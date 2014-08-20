# Student Number: PRTNIC017
# Date: 3/28/14


def print_square():
    print(5 * '*')
    for row in range(5 - 2):
        print('*', ' ' * (5 - 2), '*', sep='')
    print(5 * '*')


def print_rectangle(w, height):
    print('*' * w)
    for row in range(height - 2):
        print('*', ' ' * (w - 2), '*', sep='')
    print('*' * w)


def get_rectangle(w, height):
    returned = ('*' * w)
    for row in range(height - 2):
        returned += '\n*' + (' ' * (w - 2)) + '*'
    returned += '\n' + ('*' * w)
    return returned

def get_rectangle(width,height):
    rectangle = ''
    rectangle += '*' * width + '\n'
    for i in range(0, height - 2):
        rectangle += '*' + ' ' * (width - 2) + '*' + '\n'
    rectangle += '*' * width
    return rectangle

def print_rectangle(width,height):
    print(get_rectangle(width, height))    

def print_square():
    print_rectangle(5, 5)
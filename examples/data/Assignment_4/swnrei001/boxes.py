def get_rectangle(width, height):
    top_bottom = '*'*width
    mid = ('*' + ' ' * (width - 2) + '*\n')*(height - 2)
    return top_bottom + '\n' + mid + top_bottom

def print_rectangle(width, height):
    print(get_rectangle(width, height))

def print_square():
    print_rectangle(5, 5)
    

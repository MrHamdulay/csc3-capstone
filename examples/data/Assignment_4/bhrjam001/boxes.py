def get_rectangle(w, h):
    output = '*' * w + '\n'
    for i in range(0, h - 2):
        output += '*' + ' ' * (w - 2) + '*' + '\n'
    output += '*' * w
    return output

def print_rectangle(w, h):
    print(get_rectangle(w, h))
        
def print_square():
    print_rectangle(5, 5)
def print_square():
    print('*' * 5)
    
    for k in range(3):
        print('*   *')
    
    print('*' * 5)
    
def print_rectangle (w, h):
    print('*' * w)
    
    for k in range(h - 2):
        print('*' + ' ' * (w - 2) + '*')
        
    print('*' * w)
    
def get_rectangle(w, h):
    box = '*' * w + '\n'
    for k in range(h - 2):
        box += '*' + ' '* (w - 2) + '*' + '\n'
    box += '*' * w + '\n'
    print(box)
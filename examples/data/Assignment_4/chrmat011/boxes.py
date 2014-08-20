def print_square():
    print('*'*5)
    for i in range(3):
        print('*   *')
    print('*'*5)

def print_rectangle(w, h):
    print('*'*w)
    for i in range(h-2):
        print('*',' '*(w-2),'*',sep='')
    if h>1: print('*'*w)

def get_rectangle(w,h):
    s = '*'*w + '\n'
    for i in range(h-2):
        s = s + '*' + ' '*(w-2) + '*' + '\n'
    if h>1: s = s + '*'*w
    return s

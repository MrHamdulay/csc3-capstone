
def print_square():
    x = 5
    a = '*' 
    b = ' '* (x-2)
    
    for i in range(x):
        if (i == 0):
            print('*' * x)
        elif i == (x-1):
            print('*' * x)
            
        else:
            print(a+b+a)
            
            
def print_rectangle(width,height):
    #d = eval(height)
    #c = eval(width)
    b = ' ' * (width - 2)
    a = '*'
    for i in range(height):
        if i == 0:
            print(a * width)
        elif i == height - 1:
            print(a * width)
        else:
            print(a+b+a)
    


def get_rectangle(w,h):
    box = '*'*w+'\n'
    for i in range (h-2):
        box += '*'+' '*(w-2)+'*\n'
    for i in range(w):
        box += '*'
    return box


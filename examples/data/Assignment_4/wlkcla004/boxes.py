def print_square():
    print('*'*5)
    print('*   *')
    print('*   *')
    print('*   *')
    print('*'*5)


def print_rectangle(w,h):
    print('*'*w)
    for i in range(h-2):
        print('*'+' '*(w-2)+'*')    
    print('*'*w)

        
 


def get_rectangle(w,h):
    n=int(w)
    x=""
    for i in range(w):
        x+='*'
    x+='\n'
    for i in range(h-2):
        x+='*'
        for j in range(w-2):
            x+=' '
        x=x+'*'+'\n'
    for i in range(w):
        x+='*'
    return x


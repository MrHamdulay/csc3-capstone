def print_square():
    print('*****')
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')

def print_rectangle(w,h):
    gap = w-2
    print('*'*w)
    for i in range (h-2):
        print('*', gap*' ', '*',sep = '')
    print('*'*w)
    
def get_rectangle(w,h):
    a = ('*'*w+'\n')
    gap = w-2
    for i in range (h-2):
        a +='*'+gap*' '+ '*'+'\n'
    a+='*'*w
    return a
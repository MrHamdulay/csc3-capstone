def print_square():
    x=5
    print('*'*x)
    for i in range(x-2):
        print('*',' '*(x-4),'*')
    print('*'*x)     
    
def print_rectangle(w,h):
    print('*'*w)
    for i in range(h-2):
        print('*',' '*(w-2),'*',sep='')
    print('*'*w,sep=' ')        
        
def get_rectangle(w,h):
    x = '*'*w+'\n'
    for i in range((h-2)):
        x += '*'+' '*(w-2)+'*'+'\n'
    x += '*'*w
    return x
def print_square():
    side=5
    print(side*'*')
    for i in range (3):
        print('*',' '*3,'*',sep='')
    print(side*'*')
    
def print_rectangle(w,h):
    space=w-2
    print(w*'*')
    for i in range(h-2):
        print('*',' '*space,'*',sep='')
    print(w*'*')

def get_rectangle(w,h):
    space=w-2
    a=(w*'*')
    for i in range(h-2):
        a+=('\n*'+' '*space+'*')
    a+=('\n'+w*'*')  
    return a

    

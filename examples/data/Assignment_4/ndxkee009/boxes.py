def print_square():
    print('*'*5)
    
    for i in range (0,3):
        print('*   *')
        
    print('*'*5)
        
def print_rectangle(y,z):
    
    print('*'*y)
    
    for i in range(0,z-2):
        print('*' + ' '*(y-2) +'*')
        
    print('*'*y)
    
def get_rectangle(w,h):
    s=""   
    s+=('*'*w +"\n")
    for i in range(0,h-2):
        s+=('*'+' '*(w-2)+'*'+"\n")
    s+=('*'*w)    
    
    return s
    
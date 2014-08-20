def print_square():
    print('*****')
    print('*   *')
    print('*   *')
    print('*   *')
    print('*****')
    
def print_rectangle(w,h):
    for i in range(1,h+1):
        if i ==1 or i==h: 
            print(w*'*')
        else: 
            print('*',' '*(w-2),'*', sep='')
            
def get_rectangle(w,h):
    rectangle=''
    for i in range(1,h+1):
        if i ==1 or i==h: 
            rectangle+=w*'*'+'\n'
        else: 
            rectangle+='*'+' '*(w-2)+'*\n' 
    return rectangle
def print_square():
    print(5*'*')
    for i in range(0,3):
        print('*   *')
    print(5*'*')
    
def print_rectangle(w, h):
    print(w*'*')
    for i in range(0,h-2):
            print('*'+ ' '*(w-2)+'*',sep='')
    print(w*'*')
    

def get_rectangle(w,h):
    b=""
    a=(w* "*"+"\n")
    for i in range(h-2):
        b+="*"+(w-2)*" "+"*"+"\n"
    c=w*"*"
    return a+(b)+c
   
   



def print_square():
    
    top="*"*5
    mid="*"+" "*(3)+"*"
    print(top)
    print((mid))
    print((mid))
    print((mid))
    print(top)

def print_rectangle(w,h):
    
    top="*"*w
    mid="*"+" "*(w-2)+"*"
    
    print(top)
    
    for i in range(h-2):
        print(mid)
    
    print(top)
    
def get_rectangle(w,h):
    
    top="*"*w
    mid="*"+" "*(w-2)+"*"
    box=top+"\n"
    
    for i in range(h-2):
        
        if(i!=(h-2)):
            box+=mid+"\n"
        
        else:
            box+=mid
            
    box+=top
    
    return box        
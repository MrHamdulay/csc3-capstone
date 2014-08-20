"""
Adam Oosthuizen
Module for Assignment4
31 March 2014
"""
s = "*"
def print_square():
    s = "*"
    print(5*s)
    print(s+3*" "+s)
    print(s+3*" "+s)
    print(s+3*" "+s)
    print(5*s)
    
def print_rectangle (w, h):
    print(w*s)
    
    for i in range (1, h-1,1):
        print(s+(w-2)*" "+s)    
        
    print(w*s)     

def get_rectangle (w, h):
    r  = (w*s)
    
    for i in range (1, h-1,1):
        r+=("\n"+s+(w-2)*" "+s)    
        
    r+=("\n"+w*s)     
    return r

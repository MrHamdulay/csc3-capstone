

def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width,height):
    for i in range(height):
        if i==0 or i==(height-1):
            print(width*"*")
        else:
            print("*"+(width-2)*" "+"*")
            
def get_rectangle(width,height):
    sss = ""
    for i in range(height-1): 
        if i==0:
            sss = sss + ("*"*(width)) + "\n"
        if i==(height-2):
            sss = sss + ("*"*(width))        
        else:
            sss = sss + ("*"+" "*(width-2)+"*") + "\n"
    return sss
            
    
        
    
    
def print_square ():
    print("*"*5)
    print(3*("*"+" "*3+"*\n"), end="")
    print("*"*5)

def print_rectangle (w, h):
    for i in range(h): 
        if i==0 or i==(h-1):
            print("*"*w)
        else:
            print("*"+" "*(w-2)+"*")
                  
def get_rectangle (w, h):
    x=""
    for i in range(h): 
        if i==0:
            x+="*"*w+"\n"
        elif i==(h-1) :x+="*"*w
        else:
            x+="*"+" "*(w-2)+"*\n"    
            
    return x
def print_square():
    for i in range (5):
        if(i==0) or (i==4):
            print(5*"*")
        else:
            print("*   *")

def print_rectangle(w,h):
    for i in range(h):
        if(i==0) or (i==(h-1)):
            print(w*"*")
        else:
            print("*"+(w-2)*" "+"*")

def get_rectangle(w,h):
    R=""
    for i in range(h):
            if(i==0) or (i==(h-1)):
                R= R+ (w*"*")
             
            else:
                R= R+("*"+(w-2)*" "+"*")   
                
            R= R+ "\n"
    return R
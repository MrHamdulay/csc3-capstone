def print_square():
    for i in range(1,6):
        if (i==1) or (i==5):
            print("*"*5)
        else:
            print("*","*", sep="   ")

def print_rectangle(W,H):
    j=0
    while j < H:
        if j==0:
            print("*"*W)
        elif j== H-1:
            print("*"*W)
        else:
            space = " "*(W-2)
            string= "*" + space + "*"
            print(string)
        j+=1

def get_rectangle(W,H):
    inner =  ""
    k=0
    line = "\n"
    if H <=2:
        string = "*"*W + line + "*"*W
    else:
        for k in range(0,(H-2)):
            if k == 0:
                inner = inner + "\n" 
            inner= inner + "*" + (" "*(W-2)) + "*" 
            if k == (H-1):
                break
            else:
                inner = inner + "\n"            
            string= "*"*W + inner + "*"*W 
    return string
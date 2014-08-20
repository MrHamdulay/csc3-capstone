# 
def get_rectangle (w, h):
    s = ""
    for j in range (h):
            if (j == 0 or j == h-1):
                s += ("*"*w + "\n")
            else:
                s += ("*" + " "*(w-2) + "*" + "\n")
    return s
def print_rectangle (w, h):
    for k in range (h):
        if (k == 0 or k == h-1):
            print("*"*w)
        else:
            print("*" + " "*(w-2) + "*",sep='')
def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

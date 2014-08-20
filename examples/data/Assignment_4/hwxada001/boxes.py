def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
def print_rectangle (w, h):
    for i in range (h):
        if (i == 0 or i == h-1):
            print("*"*w)
        else:
            print("*" + " "*(w-2) + "*",sep='')
def get_rectangle (w, h):
    s = ""
    for i in range (h):
            if (i == 0 or i == h-1):
                s += ("*"*w + "\n")
            else:
                s += ("*" + " "*(w-2) + "*" + "\n")
    return s
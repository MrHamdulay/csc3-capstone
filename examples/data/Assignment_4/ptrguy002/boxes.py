def print_square():
    print_rectangle(5, 5)

def print_rectangle(w, h):
    print(get_rectangle(w, h))

def get_rectangle(w, h):
    ret = ""
    for i in range(0, h):
        if i > 0 and i < h-1:
            ret += "*" + " "*(w-2) + "*"
        else:
            ret += "*"*(w)
        if i < h-1:
            ret += "\n"
    return ret

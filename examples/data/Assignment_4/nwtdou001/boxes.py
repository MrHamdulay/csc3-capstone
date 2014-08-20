def print_square():
    print("*****")
    for i in range(0,3):
        print("*   *")
    print("*****")

def print_rectangle(w,h):
    print("*"*w)
    for i in range(0,h-2):
        print("*"+" "*(w-2)+"*")
    print("*"*w)

def get_rectangle(w,h):
    rect = ""
    rect += "*"*w + "\n"
    for i in range(0,h-2):
        rect += "*"+" "*(w-2)+"*\n"
    rect += "*"*w + ""
    return rect
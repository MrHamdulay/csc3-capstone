def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

def print_rectangle(width, height):
    for i in range(1,height+1):
        if i == 1: print("*"*width)
        elif i == height: print("*"*width)
        else: print("*"+" "*(width-2)+"*")

def get_rectangle(width, height):
    for i in range(1,height+1):
            if i == 1: output = ("*"*width)+"\n"
            elif i == height: output+=("*"*width)+"\n"
            else: output+=("*"+" "*(width-2)+"*")+"\n"
    return output

    
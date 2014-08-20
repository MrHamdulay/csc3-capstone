def print_square():
    print(get_rectangle(5, 5))

def print_rectangle(width, height):
    print(get_rectangle(width, height))

def get_rectangle(width, height):
    s = "*"*width +"\n"
    for i in range(height-2):
        s += "*" + " "*(width-2) + "*\n"
    s+= "*"*width
    return s

#if __name__ == '__main__':
    #print_square()
    #print_rectangle(6, 8)
    #print(get_rectangle(10, 12))
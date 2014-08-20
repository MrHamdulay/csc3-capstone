def print_square():
    print("*****\n*   *\n*   *\n*   *\n*****")

def print_rectangle(width,height):
    print('*'*width)
    for i in range(height-2):
        print('*'+" "*(width-3),"*")
    print('*'*width)


def get_rectangle (width, height):
    return ("*"*width)+"\n"+(height-2)*(("*"+" "*(width-2)+"*")+"\n")+("*"*width)
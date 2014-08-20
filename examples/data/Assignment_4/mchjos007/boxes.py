def print_square ():
    print("*****")
    for i in range(3):
        print("*   *")
    print("*****")
def print_rectangle (width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"+" "*(width-2) + "*")
    print("*"*width)
def get_rectangle (width, height):
    box = ""
    box += "*"*width +"\n"
    for i in range(height-2):
        box += "*"+" "*(width-2) + "*"+"\n"
    box += "*"*width 
    return box
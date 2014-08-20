def print_square():
    height = 5
    width = 5
    print("*"*width)
    for i in range(2,height):
        print("*"+" "*(width-2)+"*")
    print("*"*width)

def print_rectangle(width,height):
    print("*"*width)
    for i in range(2,height):
        print("*"+" "*(width-2)+"*")
    print("*"*width)

def get_rectangle(width,height):
    rectangle = ""
    for i in range(height):
        if i==0:
            rectangle = rectangle+"*"*width+"\n"
        elif i==(height-1):
            rectangle = rectangle+"*"*width
        elif 0<i<(height-1):
            rectangle = rectangle+"*"+" "*(width-2)+"*"+"\n"
    return rectangle
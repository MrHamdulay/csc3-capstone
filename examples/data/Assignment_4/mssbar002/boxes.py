
def print_square():
    i = 5
    while i > 0:
        if i == 5 or i == 1:
            print("*****")
            i -= 1
        else:
            print("*   *")
            i -= 1
            
def print_rectangle(width, height):
    w = width
    h = height
    while h > 0:
        if h == height or h == 1:
            print("*"*width)
            h -= 1
        else:
            print("*" + " "*(width-2) + "*")
            h -= 1
            
def get_rectangle(width, height):
    w = width
    h = height
    figure =""
    while h > 0:
        if h == height or h == 1:
            figure += "*"*width + "\n"
            h -= 1
        else:
            figure += "*" + " "*(width-2) + "*\n"
            h -= 1  
    return figure
            
    
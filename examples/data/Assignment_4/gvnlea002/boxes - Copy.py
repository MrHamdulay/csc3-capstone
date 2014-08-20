def print_square():
    print(5*"*")
    for i in range(3):
        print("*   *")
    print(5*"*")

def print_rectangle(width,height):
    print(width*"*")
    for i in range(height-2):
        print("*"+(width-2)*" "+"*")
    print(width*"*")

def get_rectangle(width,height):
    figure = (width*"*")
    for i in range(height-2):
        figure = figure + ("\n*"+(width-2)*" "+"*")
    figure = figure + ("\n"+width*"*")
    return figure

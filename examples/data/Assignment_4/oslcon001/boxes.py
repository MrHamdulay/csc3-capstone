# Conor O'Sullivan
# Prints Boxes
# 4/01/2014
def print_square ():
    print("*****\n*   *\n*   *\n*   *\n*****")

def print_rectangle (width, height):
    print("*"*width)
    for x in range(height-2):
        print("*" + " "*(width-2) + "*")
    
    print("*"*width)

def get_rectangle (width, height):
    figure = "*"*width + "\n"
    for x in range(height-2):
        figure+= "*" + " "*(width-2) + "*" +"\n"
    
    figure += "*"*width
    return figure

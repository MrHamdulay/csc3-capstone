"""functions that print hollow boxes of stars"""

def print_square():
    print("*****")
    for i in range(3):
        print("*   *")
    print("*****")
    
def print_rectangle(width, height):
    print("*" * width)
    for i in range(height - 2):
        print("*", " " * (width - 2), "*", sep = "")
    print("*" * width)
    
def get_rectangle(width, height):
    box_string = ""
    box_string += "{}{}".format("*" * width, "\n")
    for i in range(height -2):
        box_string += "*{}*{}".format(" " * (width -2), "\n")
    box_string += "{}{}".format("*" * width, "\n")
    return box_string

    
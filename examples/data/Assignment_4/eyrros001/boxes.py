def print_square():
        print("*****","*   *","*   *","*   *","*****", sep="\n")
        
        
def print_rectangle (width, height):
        print("*"*width)
        for i in range(height-2):
                print("*" + " "*(width-2) + "*")
        print("*"*width)
        
def get_rectangle(width, height):
        rect = "*"*width
        for i in range(height-2):
                rect += "\n" + "*" + " "*(width-2) + "*"
        rect += "\n" + "*"*width
        return rect

    
def print_square ():
    print("*****")   
    for i in range (0,3):
        print("*   *")
    print("*****")
    
def print_rectangle (width, hight):
    print("*"*width)
    for i in range (0, hight-2):
        print("*" + " "*(width-2) + "*")    
    print("*"*width)
    
def get_rectangle (width, hight):
    Rect = ""
    Rect = Rect + "*"*width + "\n"
    for i in range (0, hight-2):
        Rect = Rect + "*" + " "*(width-2) + "*\n"
    Rect = Rect + "*"*width
    return Rect
#Q1 Assignment 4
#KVRSHA004
#Shaheel Kooverjee

def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width, height):
    print(width*"*")
    for i in range(height-2):
        print("*"+" "*(width-2)+"*")
    print(width*"*")
    
def get_rectangle(width, height):
    rectangle = "*"*width
    for i in range(2, height):
        rectangle = rectangle + "\n" + "*" + (" "*(width-2)) + "*"
    rectangle = rectangle + "\n" + "*"*width
    return rectangle
#VRMNIC005
#Assignment 4 question 1

def print_square ():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

def print_rectangle(width, height):
    print("*"*width) #prints top row
    for i in range(height-2): #prints middle rows
        print("*", " "* (width- 2), "*", sep="")
    print("*" * width) #prints bottom row
    
def get_rectangle(width, height):
    box = ""
    box += (("*"* width) + "\n") #concatenate top row
    for i in range(height-2): #concatenate middle rows
        box += ("*" + (" " * (width - 2)) + "*" + "\n")
    box += (("*" * width) + "\n") #concatenates bottom row
    return box

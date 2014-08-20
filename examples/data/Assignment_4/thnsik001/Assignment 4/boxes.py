"""assignment4
question1
THNSIK001"""

def print_square():
    print("*****")
    for i in range(3):
        print("*   *")
    print("*****")
    
def print_rectangle(a,b):
    print("*"*a)
    for i in range((b-2)):
        print("*",sep="",end="")
        print(" "*(a-2),end="")
        print("*")
    print("*"*a)

def get_rectangle(a,b):
    rect = "*"*a
    rect += "\n"
    for i in range((b-2)):
        rect += "*"
        rect += " "*(a-2)
        rect += "*\n"
    rect += "*"*a
    return rect

"""create hollow boxes of stars
tim hardie
31/3/14"""

def print_square():
    #print("*"*5,"\n*   *"*3,"\n","*"*5,sep='')
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

def print_rectangle(x,y):
    print(x*"*")
    for i in range(y-2):
        print("*"," "*(x-2),"*",sep='')
    print(x*"*")

def get_rectangle(x,y):
    rect = "*"*x
    for i in range(y-2):
        rect += "\n*" +" "*(x-2) +"*"
    rect += "\n" + "*"*x
    return rect
    
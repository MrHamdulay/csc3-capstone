#module boxes

def print_square ():
    print("*"* 5)
    for i in range(3):
        print("*" + " "*3 + "*")
    print("*"* 5 + "\n")

def print_rectangle(x,y):
    print("*" * x)
    for i in range(y - 2):
        print("*" + " "*(x - 2) + "*")
    print("*" * x)

def get_rectangle (x, y):   
    rectangle = "*" * x + "\n"
    for i in range(y - 2):  
        rectangle = rectangle + "*" + " "*(x - 2) + "*\n"  
    rectangle = rectangle + "*" * x
    return rectangle
    


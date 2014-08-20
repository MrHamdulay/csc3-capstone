# Boxes
# Michele Balestra BLSMIC004

def print_square():
    print("*****")
    for i in range(3):
        print("*   *")
    print("*****")
    
def print_rectangle(x,y):
    print("*"*x)
    for i in range(y-2):
        print("*" + " "*(x-2) + "*")
    print("*"*x)
    
def get_rectangle(a,b):
    return("*"*a + "\n" + ("*" + " "*(a-2) + "*\n")*(b-2) + "*"*a)
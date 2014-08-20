#Tevin Chetty
#CHTTEV001
#Assignment 4
#boxes

def print_square():
    print("*****")
    for i in range(3):
        print("*   *")
    print("*****")

def print_rectangle(width, height):
    print(width*"*")
    for i in range(height-2):
        print("*"," "*(width-2),"*", sep="")
    print(width*"*")
    
def get_rectangle(width, height):
    x = '*' * (width) + '\n'
    x += ('*' + ' ' * (width - 2) + '*\n') * (height - 2)
    x += '*' * (width) + '\n'
    return x

#Module for question1
def print_square():
    print("*"*5)
    for i in range(3):
        #print("*"*5)
        print("*"+" "*3+"*")
    print("*"*5)
def print_rectangle(width,height):
    print("*"*width)
    for i in range(height-2):
        #print("*"*width)
        print("*"+" "*(width-2)+"*")
    print("*"*width)
def get_rectangle(width,height):
    width_new=width-2
    a=(width*'*'+'\n')
    b=('*'+width_new*' '+'*'+'\n')*(height-2)
    c=(width*'*'+'\n')
    return a+b+c

daniel = 'Daniel'
__author__ = daniel
def print_square():
    print("*****")
    for i in range(3):
        print("*",' ',"*")
    for i in range (5):
        print ("*",end='')

def print_rectangle(w,h):
    rectangle="*"*w+'\n'
    for i in range(h-2):
        rectangle+='*'+' '*(w-2)+'*\n'
    for i in range (w):
        rectangle+='*'
    print(rectangle)

def get_rectangle(w,h):
    box='*'*w+'\n'
    for i in range (h-2):
        box+='*'+' '*(w-2)+'*\n'
    for i in range(w):
        box+='*'
    return box
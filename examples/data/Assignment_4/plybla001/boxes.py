#Assigment 4 Q1
#B.Player
#30/03/2014

def print_square():    
    print("*"*5)
    for i in range(3):
        print('*'+' '*3+'*')
    print("*"*5)


def print_rectangle(w,h):
    print("*"*w)
    for i in range(h-2):
        print('*'+' '*(w-2)+'*')
    print("*"*w)    


def get_rectangle(w,h):
    rect="*"*w
    for i in range(h-2):
        rect=rect+"\n"+'*'+' '*(w-2)+'*'
    rect = rect +("\n"+"*"*w)    
    return rect



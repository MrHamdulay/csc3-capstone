# question 1 

def print_square():
    print('*'*5)
    for row in range(3): 
        print('*'+(' '*3)+'*')
    print('*'*5)
    

def print_rectangle(width, height):
    
    print('*'*width)
    for row in range (height-2):
        print('*'+(' '*(height-3))+'*')
    print('*'*width)


def get_rectangle(width,height): 
    box = ('*' * width)+"\n"
    for row in range (height-2):
        box = box+ '*'+(' '*(height-3))+'*'+"\n" 
    box = box+('*'*width)
    return box 

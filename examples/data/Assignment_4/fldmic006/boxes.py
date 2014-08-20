def print_square():
    
    print('*'*5)
    
    for i in range(3):
        print('*', ' '*3, '*', sep = '')
    
    print('*'*5)

def print_rectangle(width, height):
    
    #top layer
    print('*'*width)
    
    #sides
    gap = width-2
    for j in range((height-2)):
        print('*', ' '*gap, '*', sep = '')
    
    #bottom layer
    print('*'*width)

def get_rectangle(width, height):
    
    box = ""
    
    box += '*'*width
    box += "\n"
    
    #sides
    for i in range((height-2)):
        box += '*' + ' '*(width-2) + '*\n'
        
    box += '*'*width
    
    return box
    
def print_square():

    gap = 3

    for i in range(0,5):
        if i == 0 or i == 4:
            print('*' * 5)
            
        else:
            print('*'+(gap*' ')+'*')            


def print_rectangle(width,height):
    
    
    for i in range(0,height):
        if i == 0 or i == (height-1):
            print('*' * width)
                
        else:
            print('*'+((width-2)*' ')+'*')
            
def get_rectangle(width,height):
    
    w = '*' * width
    #v = ('*'* 1) + (' '* (width-2)) + ('*'*1)
    
    for i in range(height-2):
            w = w+"\n"+"*"+(" "*(width-2))+"*"
    w = w+"\n"+"*"*width
    return w
            
get_rectangle(3,3)            
                
            
            
            


    
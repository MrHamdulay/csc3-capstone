
#Mlangeni 



def print_square():
        a = 5
        b = 0
        for i in range(4):
                print("*"*a+("*"+" "*(3)+"*")*b)
                a = 0
                b = 1
        for i in range(1):
                print("*"*5)
        
def print_rectangle(width, height):
        a = width
        b = 0
        for i in range(height-1):
                print("*"*a+("*"+" "*(width-2)+"*")*b)
                a = 0
                b = 1
        for i in range(1):
                print("*"*width)
    

def get_rectangle(width, height):
        new = ''
        new = '*'*width+'\n'
        b = width
        a = height
        for i in range(a-2):
                new = new + '*'+' '*(b-2)+'*\n'
        new = new + '*'*b  
        return new
    
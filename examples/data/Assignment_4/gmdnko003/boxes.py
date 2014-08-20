def print_square():
        print("*"*5)
        print("*"," "*3,"*",sep="")
        print("*"," "*3,"*",sep="")
        print("*"," "*3,"*",sep="")
        print("*"*5)
    
def print_rectangle(width, height):
        print("*"*width)
        for i in range(2,height):
                print("*"," "*(width-2),"*",sep="")
        print("*"*width)
    
def get_rectangle(width, height):
        print_rectangle(width, height)
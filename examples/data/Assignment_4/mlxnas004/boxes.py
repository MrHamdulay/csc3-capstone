def print_square():
    print ("*****")
    for i in range(3):
        print("*   *")
    print ("*****")
    
def print_rectangle(width,height):
    print("*"*width+"\n"+("*"+" "*(width-2)+"*\n")*(height-2)+"*"*width)

def get_rectangle(width,height):
    a = ("*"*width+"\n"+("*"+" "*(width-2)+"*\n")*(height-2)+"*"*width)
    return a



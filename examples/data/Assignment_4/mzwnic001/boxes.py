def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width,height):
    print("*"*width)
    while height > 2:
        print("*"," "*(width-2), "*", sep="")
        height=height-1
    print("*"*width)

def get_rectangle(width,height):
    rectangle=""
    rectangle=rectangle+"*"*(width)+("\n"+"*"+" "*(width-2)+"*")*(height-2)+"\n"+"*"*(width)
    return rectangle
    

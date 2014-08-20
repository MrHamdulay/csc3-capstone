def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*", " "*(width-2), "*", sep="")
    print("*"*width)
    
def get_rectangle(width, height):
    a="*"*width+"\n"
    b=("*" + " "*(width-2) + "*\n")*(height-2)  
    c="*"*width
    return a + b + c

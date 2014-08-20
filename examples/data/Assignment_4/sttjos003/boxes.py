def print_square():
    print("*****\n*   *\n*   *\n*   *\n*****")
    
def print_rectangle(width,height):
    print("*"*width)
    i=1
    while i<height-1:
        print("*", " "*(width-2), "*", sep="")
        i=i+1
    print("*"*width)
    
def get_rectangle (width, height):
    t=("*"*width+"\n")
    i=1
    r=""
    while i<height-1:
        q=" "*(width-2)
        r=r+"*"+q+"*\n"
        i=i+1
    result=t+r+t
    return result
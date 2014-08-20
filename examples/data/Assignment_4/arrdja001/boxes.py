def print_square():
    print("*"*5)
    for i in range(3): print("*","*", sep = "   ")
    print("*"*5)
        
    
def print_rectangle(width,height):
    if width == 0 or height == 0: print()
    elif height == 1: print("*"*width)
    if width == 1:
        for i in range(height): print("*")
    else:
        print("*"*width)
        for i in range(height - 2):
            print("*","*", sep = (" " * (width - 2)))
        print("*"*width)
        
def get_rectangle(width,height):
    outside = "*" * width + "\n"
    inside = ("*" + " " * (width-2) + "*" + "\n")*(height-2)
    box_c = outside + inside + outside
    return(box_c)

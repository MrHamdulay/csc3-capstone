# program to print 5x5 hollow box

def print_square() :
    
    side = 5
    hollow_inside = side - 2

    print("*" * side) 
    
    for i in range(side - 2) : 
        print("*" + " " * hollow_inside + "*")
        
    print("*" * side)
    
    
    
# program to print hollow box with given width and height

def print_rectangle(width, height) :
    
    print("*" * width)
    
    hollow_inside_2 = width - 2
    for i in range(height - 2) :
        print("*" + " " * hollow_inside_2 + "*")
    
    print("*" * width)
    


# program that returns a string containing a box with given height

def get_rectangle(width, height) :
    
    x = "*" * width + "\n"
    hollow_inside_2 = width - 2
    y = ("*" + " " * hollow_inside_2 + "*" + "\n")
    
    return(x + y*(height-2) + x)
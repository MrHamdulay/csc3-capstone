def print_square():
    print("*"*5)
    for i in range(3):
        print("*", " ", "*")
    print("*"*5)
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*", " "*(width-2), "*", sep="")
    print("*"*width)
    
def get_rectangle(width, height):
    y= ("*"*width + "\n")
        
    x=0
    while x<height-2:
        y+= ("*"+(" "*(width-2)+"*")+"\n")
        x+=1
        
    y+= ("*"*width)
    return (y)
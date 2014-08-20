def print_square ():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle (width, height):
    print("*"*width)
    for i in range (height-2):
        print("*"+" "*(width-2)+"*")
    print("*"*width)
   
def get_rectangle (width, height):
    #must be done sepreately, return everything
    #return must be stringy
    box=""
    
    top = ("*"*width+"\n")
    
    middle=""
    for i in range (height-2):
        line = ("*"+" "*(width-2)+"*" + "\n")
        middle += line
    end = ("*"*width)
    box = top + middle + end
    return str(box)


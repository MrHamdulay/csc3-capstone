def print_square ():
    print ("*****")
    print ("*   *")
    print ("*   *")
    print ("*   *")
    print ("*****")
    
    
    
def print_rectangle(width,height):
    print("*" * width)
    for i in range(height-2):
        print ("*"+' '* (width-2)+"*")
    print("*" * width)
    
    
    
def get_rectangle(width,height):
    top='*'*width+'\n'
    for i in range(height-2):
        top= top+'*'
        for i in range(width-2):
            top =top+' '
        top= top+'*\n'
    top = top +'*'*width

    return top

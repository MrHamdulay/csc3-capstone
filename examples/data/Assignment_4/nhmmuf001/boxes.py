def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****") 



def print_rectangle(width,height):
    if width<0:
        width = width*-1
        print("*"*width)
    else:
        print("*"*width)
    if height<0:
        height = height*-1        
    for i in range(height-2):
            print("*"," "*(width-2),"*",sep="")
    print("*"*width)
    



def get_rectangle(width,height):
    
    if width<0:
        width = width*(-1)
        add_next = "*"*width
    else:
        add_next = "*"*width
    if height<0:
        height = height*-1
    for i in range(height-2):
        add_next = add_next+"\n" + ("*"+(" "*(width-2))+"*")
    add_next = add_next+"\n" + ("*"*width)
    return add_next
    
    
    
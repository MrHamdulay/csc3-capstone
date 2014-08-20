def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width,height):
    print("*"*width)
    for i in range (height-2):
        sp=" "*(width-2)
        print("*",sp,"*",sep="")
    print("*"*width)
    
def get_rectangle(width,height):
    sq="*"*width+"\n"
    sp=" "*(width-2)
    for i in range (height-2):
        sq=sq+"*"+sp+"*"+"\n"
    sq=sq+"*"*width
    return sq 
        
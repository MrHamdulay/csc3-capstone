#Boxes
#Sofia Palmer
#31 March 2014

def print_square():
    print("*" * 5)
    print("*" + " " * 3 + "*")
    print("*" + " " * 3 + "*")
    print("*" + " " * 3 + "*")
    print("*" * 5)
    
def print_rectangle(width,height):
    print("*" * width)
    for i in range(0,height-2):
        print("*" + " " * (width - 2) + "*")
    print("*" * width)
    
def get_rectangle(width,height):
    a="*" * width
    for i in range(0,height-2):
        a+="\n"+("*" + " " * (width - 2) + "*")
    a+="\n" + ("*" * width)
    return a




    

    

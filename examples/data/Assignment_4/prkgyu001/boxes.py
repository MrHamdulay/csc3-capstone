five_stars="*****"
hollow=    "*   *"


def print_square():
    print(five_stars)
    print(hollow)
    print(hollow)
    print(hollow)
    print(five_stars)
    

def print_rectangle(width,height):
    for i in range(height):
        if i == 0 or i == (height-1):
            print("*" * width)
            
        else:
            print("*", " "*(width-2), "*" , sep="")







def middle(width,height):
    for i in range(height-2):
        return("*"," "*(width-2),"*")

def topandend(width,height):
    return("*"*width)
            
def get_rectangle(width,height):
    topandend(width,height)
    middle(width,height)
    topandend(width,height)
        


            
    




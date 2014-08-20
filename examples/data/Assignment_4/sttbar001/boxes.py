def print_square():
    for i in range(5):
        if i ==0 or i == 4:
            print("*"*5)
        else:
            print("*   *")

def print_rectangle (width, height):
    for i in range(height):
            if i ==0 or i == height-1:
                print("*"*width)
            else:
                print("*"+(" "*(width-2))+"*")

def get_rectangle (width, height):
    x = ""
    for i in range(height):
                if i ==0 or i == height-1:
                    x=x+("*"*width+"\n")
                else:
                    x=x+("*"+(" "*(width-2))+"*\n") 
    return x
                    
def print_square():
   # for j in range(5):
        print("*"*5)
        print("*" + " "*3+ "*")
        print("*" + " "*3+ "*")
        print("*" + " "*3+ "*")
        print("*"*5)
def print_rectangle(width,height):
        print("*"*width)
        for j in range(height-2):
                print("*" + " "*(width-2)+ "*")
        print("*"*width)                
                
def get_rectangle(width,height):
        rect=""
        rect= ("*"*width)
        for j in range(height-2):
                rect= rect+("\n*" + " "*(width-2)+ "*")
        rect=rect+"\n"+ ("*"*width)
        return rect
        
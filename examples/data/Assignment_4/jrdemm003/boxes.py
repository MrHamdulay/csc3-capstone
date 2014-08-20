def print_square():
        print("*****")
        print("*   *")
        print("*   *")
        print("*   *")
        print("*****")
        
#print_square()
    

def print_rectangle(width,height):
        
        print("*"*width)
        x=0
        while x<=height-3:
                print("*"+(" "*(width-2)+"*"))
                x=x+1
        print("*"*width)                



def get_rectangle(width,height):
        y= ("*"*width + "\n")

        x=0
        while x<height-2:
                y+= ("*"+(" "*(width-2)+"*" + "\n"))
                x=x+1
                
        y+= ("*"*width)
        return y

if '__name__'=="__main__":
        print_square()
        print_rectangle()
        get_rectangle()
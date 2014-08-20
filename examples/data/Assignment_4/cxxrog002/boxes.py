def print_square():
        print(get_rectangle(5,5))


def print_rectangle (width, height):
        print(width*"*")
        for i in range (height-2):
                print("*",(width-2)*" ","*",sep="")
        
        print(width*"*")
#print_rectangle(3,4)
def get_rectangle (width, height):
        b=""
        a=(width*"*"+"\n")

        for i in range (height-2):
                b+="*"+(width-2)*" "+"*"+ "\n"
            
        c=(width*"*")   
        return a+(b)+c
#print(get_rectangle(5,5))
#get_rectangle (3,4)

#print_square()
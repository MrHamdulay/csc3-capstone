def print_square():
    print_rectangle(5,5)
            
def print_rectangle(width, height):
    for i in range(1,height+1):
        if width!=1:
            if i==1 or i==height:
                print("*"*width)
            else:
                print("*",(width-2)*" ","*", sep="")
        else:
            print("*")
            
def get_rectangle(width, height):
    x=""
    for i in range(1,height+1):
        if width!=1:
            if i==1 or i==height:
                x+="*"*width
                x+="\n" #so print will create a box
            else:
                x+="*"
                x+=(width-2)*" "
                x+="*"
                x+="\n"
        else:
           x+="*"
           x+="\n"
    return x
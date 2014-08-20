def print_square():
    gap=" "*3
    line1="*"*5
    line2="*"+gap+"*"
    print(line1,end="\n")
    print(line2,end="\n")
    print(line2,end="\n")
    print(line2,end="\n")
    print(line1,end="\n")    

def print_rectangle(width,height):
    w=width
    h=height
    gap=w-2
    print("*"*w)
    for i in range(height-2):
        if w==1:
            print("*")
        elif w==2:
            print("**")
        elif w>2:
            print("*"+gap*" "+"*")
    print("*"*w)
    
    
def get_rectangle(width,height):
    line1=("*"*width)+"\n"
    gap=width-2
    line2=("*"+" "*gap+"*\n")*(height-2)
    line3=("*"*width)
    return line1+line2+line3
    

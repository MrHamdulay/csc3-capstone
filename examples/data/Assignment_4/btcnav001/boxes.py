def print_square():
    print("*****")
    for _ in range(1,4):
        print("*   *")
    print("*****")
print_square()
        
def print_rectangle(width,height):
    x=height-2
    y=width-2
    for _ in range(1):
            print(width*'*')  
    for _ in range(x):
        print("*",y*" ","*", sep="")
    for _ in range(1):
                print(width*'*')  
print_rectangle(3,4)

def get_rectangle(width,height):
    x=height-2
    y=width-2
    z=(("*"*width+"\n")+(x*("*"+y*" "+"*"+"\n"))+(width*"*"+"\n"))
    return(z)

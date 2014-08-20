def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*"+" "*(width-2)+"*")
    print("*"*width)

k=0    
def get_rectangle(width, height):
    x= "*"*width + "\n"
    y=""
    for i in range(height-2):
        k= "*"+" "*(width-2)+"*"
        y+=k + "\n"
    z=x+y+x
    return z
#if name =="__main__":
    #choice= input("Choose test:\n")
    #if choice=="a":
        #print_square()
    #elif choice== b and width and height :
        #print_rectangle(width,height)
    #elif choice == c and width and height:
        #get_rectangle(width,height)
        
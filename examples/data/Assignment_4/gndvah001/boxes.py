def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

def print_rectangle(w,h):
    for i in range(h):
        if i == 0:
            print(w*"*")
        elif i>0 and i<(h-1):
            print("*",(w-2)*" ","*",sep="")
    print(w*"*")
    
def get_rectangle(width,height):
    for i in range(height):
        if i == 0:
            print(width*"*")
        elif i>0 and i<(height-1):
            print("*",(width-2)*" ","*",sep="")
    print(width*"*") 

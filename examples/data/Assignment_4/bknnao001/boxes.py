def print_square():
    for i in range (5,6):
        print("*"*5)
    for i in range(0,3):
        print(("*"+" "*(3)+"*"))
    for i in reversed(range(5,6)):
        print("*"*5)
#print_square()
def print_rectangle(width, height):
    a=eval("width")
    b=eval("height")
    for i in range(a,a+1):
        print("*"*a)
    for i in range(0,b-2):
        print("*"+" "*(a-2)+"*")
    for i in range(a,a+1):
        print("*"*a)
#print_rectangle(3,4)

def get_rectangle(width,height):
    a=eval("width")
    b=eval("height")
    c=""
    for i in range(a,a+1):
        c+="*"*a+"\n"
    for i in range(0,b-2):
        c+=("*"+" "*(a-2)+"*")+"\n"
    for i in range(a,a+1):
        c+=("*"*a)
    return(c)
#get_rectangle(4,3)
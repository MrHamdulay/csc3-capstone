def print_square():
    print("*****")
    for i in range (3):
        print("*   *")
    print("*****")


def print_rectangle(w,h):
    print("*"*w)
    for i in range (h-2):
        print("*"+" "*(w-2)+"*")
    print("*"*w)

def get_rectangle(width,height):
    l = 2
    box = "*"*width
    while l<height:
        box=box+"\n"+"*"+(" "*(width-2))+"*"
        l=l+1
    box=box+"\n"+"*"*width
    return box 
   
        

        

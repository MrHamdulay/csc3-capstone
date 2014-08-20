def print_square():
    print("*"*5)
    for i in range(3):
        print("*   *")
    print("*"*5)

def print_rectangle(width,height):
    print("*"*width)
    a=2
    while a<height:
        print("*"," "*(width-2),"*",sep="")
        a+=1
    print("*"*width)

def get_rectangle(width,height):
    a=2
    box="*"*width
    while a<height:
        box=box+ '\n' + "*" + " "*(width-2) +"*"
        a+=1
    box=box + '\n' + "*"*width
    return box


    
    


   
    
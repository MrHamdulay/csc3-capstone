#boxes.py

def print_square():
    print("*****")
    print("*   *","*   *","*   *",sep="\n")
    print("*****")

def print_rectangle(width,height):
    print("*"*width)
    for x in range(0,height-2):
        print("*"," "*(width-2),"*",sep="")
    print("*"*width)

def get_rectangle(width,height):
    s = ""
    s = s+("*"*width)+"\n"
    for x in range(0,height-2):
        s= s+("*"+" "*(width-2)+"*"+"\n")
    s =s+("*"*width)
    return s

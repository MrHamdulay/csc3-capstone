def print_square ():
    print("*****")
    for i in range(0,3):
        print("*"," ","*")
    print("*****")
#print_sq()


def print_rectangle(w,h):
    print("*"*w)
    for i in range(0,h-2):
        print("*" + " "*(w-2) + "*")
    print("*"*w)
#print_rectangle(3,4)


def get_rectangle(w,h):
    mystr = ""
    mystr = mystr + "*"*w + "\n"
    for i in range(0,h-2):
        mystr = (mystr + "*" + " "*(w-2) + "*" + "\n")
    mystr = mystr + "*"*w + "\n"
    return mystr
#get_rectangle(4,4)
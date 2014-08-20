def print_square():
    width = 5
    height_loop = width -2
    print ("*"*width)
    for i in range(height_loop):
        print("*"," "*height_loop,"*",sep="")
    print ("*"*width)

def print_rectangle (width,height):
    a = int(width)
    b = int(height)
    for i in range (b):
        if (i==0) or (i == (b-1)):
            print("*"*a)
        else:
            print(("*")+(" "*(a-2))+("*"))

def get_rectangle (width,height):
    a = int(width)
    b = int (height)
    firstline= "*"*a
    midsection= "*" + (" "*(a-2)) + "*"
    total = firstline+"\n"+((midsection) + "\n")*(b-2)+firstline
    return total
    
    




    
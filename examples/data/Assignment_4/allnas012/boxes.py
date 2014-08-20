def print_square():
    
    y=5-2
    print(5*"*")
    for i in range(3):
        print("*"+" "*3+"*")
    print("*"*5)

def print_rectangle(width,height):
    
    x =1
    y = ("*"*width)
    z = (y+"\n")
    if width == 1:
        while x<=(height-2):
                z += ("*\n")
                x +=1
    else:
        while x<=(height-2):
            z += ("*")
            z += (" "*(width-2))
            z += ("*\n")
            x +=1
    z +="*"*width
    print(z)

def get_rectangle(width,height):
    x =1
    y = ("*"*width)
    z = (y+"\n")
    if width == 1:
        while x<=(height-2):
                z += ("*\n")
                x +=1
    else:
        while x<=(height-2):
            z += ("*")
            z += (" "*(width-2))
            z += ("*\n")
            x +=1
    z +=("*"*width)
    return z

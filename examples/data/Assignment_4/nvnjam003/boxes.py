def print_square():
    for x in range (0, 5):
        if (x == 0 or x == 4):
            print (5*"*")
        else:
            print ("*" + 3*" " + "*")
            
def print_rectangle(width, height):
    for x in range(0, height):
        if (x == 0 or x == (height-1)):
            print (width*"*")
        else:
            print ("*" + (width-2)*" " + "*")

def get_rectangle(width, height):
    rectangle = ""
    for x in range(0, height):
        if (x == 0 or x == (height-1)):
            rectangle += width*"*" + "\n"
        else:
            rectangle += "*" + (width-2)*" " + "*\n"
    return rectangle
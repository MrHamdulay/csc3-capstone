def print_square(): #prints a hollow 5x5 box
    print("*"*5 + "\n" + ("*" + " "*3 + "*\n")*3 + "*"*5)

def print_rectangle(width, height): #prints a hollow rectangle
    print("*"*width + "\n" + ("*" + " "*(width - 2) + "*\n")*(height - 2) + "*"*width)

def get_rectangle(width, height): #returns a string representing a rectangle
    str_rec = ""
    str_rec += "*"*width + "\n"
    str_rec += ("*" + " "*(width - 2) + "*\n")*(height - 2)
    str_rec += "*"*width
    return str_rec
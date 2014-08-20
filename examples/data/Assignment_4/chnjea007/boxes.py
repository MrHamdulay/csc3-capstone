# assignment 4 question 1
def print_square():
    print('''*****
*   *
*   *
*   *
*****''')
def print_rectangle(width, height):
    print("*" * width)
    for i in range (height - 2):
        print("*", " " * (width - 2), "*", sep = "")
    print("*" * width)
def get_rectangle(width, height):
    squareString = "*" * width + "\n"
    for i in range (height - 2):
        squareString += "*" + " " * (width - 2) + "*" + "\n"   
    squareString += ("*" * width)
    return squareString
#Assignment 4 - Question 1
#Jayan Smart
#April 2014

def print_square():
    print("*****")
    for i in range(3):
        print("*   *")
    print("*****")

def print_rectangle (width, height):
    box = ""
    for i in range(height):
        for j in range(width):
            if (j==0 or j==(width-1) or i==0 or i == (height-1)):
                box+='*'
            else:
                box+=' '
        if i== height-1:
            print(box)
        else:
            box+='\n'

def get_rectangle(width, height):
    box = ""
    for i in range(height):
        for j in range(width):
            if (j==0 or j==(width-1) or i==0 or i == (height-1)):
                box+='*'
            else:
                box+=' '
        box+='\n'
    return box
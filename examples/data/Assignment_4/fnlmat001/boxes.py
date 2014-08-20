# Matthew Finlayson - FNLMAT001
# 29/03/14
# Assignment 4 - Question 1
#boxes.py

def print_square():
    for i in range(5):
        if (i<1 or i>3):
            print("*"*5)
        else:
            print("*   *")

def print_rectangle(width, height):
    for i in range(height):
        if i<1 or i>=height-1:
            print("*"*width)
        else: 
            print("*"+" "*(width-2)+"*")

def get_rectangle(width, height):
    output = ""
    for i in range(height):
        if i<1 or i>=height-1:
            output+="*"*width+"\n"
        else:
            output+="*"+" "*(width-2)+"*\n"
    return output

if __name__ == "__main__":
    print(get_rectangle(10,5))
#WHTBAS001
#30-03-2014
#ASSIGNMENT 4
#QUESTION 1
# ==> boxes

def print_square():
    print("*"*5, end="\n")
    for i in range(3):        
        print("*", " "*3, sep="", end="*\n")
    print("*"*5, end="\n")
    
def print_rectangle(width, height):
    print("*"*width, sep="", end="\n")
    for i in range(height - 2):
        print("*"," "*(width-2), sep="", end="*\n")
    print("*"*width, sep="", end="\n")

def get_rectangle (width, height):
    topb = '*'*width + "\n"
    body = "*" + " "*(width-2) + "*" + "\n"
    rectangle  = topb + body*(height - 2) + topb
    return rectangle

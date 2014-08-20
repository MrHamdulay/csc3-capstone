#Program to print boxes!!
#Geoff Murphy 
#MRPGEO001
#1 April 2014


def print_square():
    print("*****",sep="")
    print("*   *",sep="")
    print("*   *",sep="")
    print("*   *",sep="")
    print("*****",sep="")
     
def print_rectangle(width, height):
    print("*"*width, sep="")
    for i in range(height - 2):
        print("*", " "*(width - 2), "*",sep="")
    print("*"*width, sep="")
    
def get_rectangle(width, height):
    x = "*"*width + "\n"
    w = width - 2
    
    y = height - 2
    if width == 2:
        for i in range(y):
            x += "**\n"
    else:
        for i in range(y):
            x += "*" + (" "*w) + "*\n"
    
    x += "*"*width
    
    return (x)
    
    
    

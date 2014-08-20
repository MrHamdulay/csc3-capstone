# Program to print hollow boxes using stars
# Nomsa Gamedze
# 31 March 2014

def print_square():
    print(5*"*", "*   *", "*   *", "*   *",5*"*", sep='\n')
    
def print_rectangle(width, height):
    print("*"*width)
    for i in range(height-2):
        print("*", " "*(width-2), "*", sep="")
    print("*"*width)

def get_rectangle(width, height):
    top_bot =  "*"*width
    walls =""
    for i in range(height-2):
            x = "*" + " "*(width-2) + "*"  + '\n'
            walls += x
    rectangle = top_bot + '\n' + walls + top_bot
    return rectangle



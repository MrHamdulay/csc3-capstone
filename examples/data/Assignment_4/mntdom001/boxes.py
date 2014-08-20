# boxes.py
# Author: Dominic Manthoko
# 30 March 2014

def print_square():
    width = 5
    print("*"*width)
    for i in range(3):
        print("*" + " "*(width-2) + "*")
    print("*"*width)
    
def print_rectangle(width,height):
    print("*" * width)
    for w in range(height-2):
        print("*" + " " *(width -2) + "*")
    print("*" * width)
    
def get_rectangle(width,height):
    figure = ""
    # this for loop will append the top part of the box into the string called figure
    for i in range(width):
        figure += "*"
    figure +="\n"
    
    # this for loop will append the middle part of the box to figure
    for x in range(height-2):                               # (height-2) because the top and bottom will be handled seperately
        figure += "*" + " " *(width-2) + "*""\n"            
        
    # this part of the loop will append the part of the box to figure
    for i in range(width):
        figure += "*"
        
    return figure 


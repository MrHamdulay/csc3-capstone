# This is a module called boxes.py and contains the three functions:

# print_square (),
#      that prints a 5x5 box on the screen

# print_rectangle (width, height), 
#      that prints a box on the screen with given width and height

# get_rectangle (width, height),
#      that returns a string containing a box with given width and height

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 28 March 2014

# print_square(prints a 5x5 box on the screen
def print_square():    
    # Prints the top 5 stars
    print("*"*5)
    for i in range(1,4):
        # Prints the middle stars
        texta = "{0}{1}{0}"
        print(texta.format("*"," "*3))
    # Prints the bottom 5 stars
    print("*"*5)

# prints a box on the screen with given width and height   
def print_rectangle(width, height):
    # Passes paramenters to local variables
    wid = int(width)
    hei = int(height)
    
    # prints the top stars
    print("*"*wid)
    for j in range(1,hei-1):
        textb = "{0}{1}{0}"
        # Prints the middle stars
        print(textb.format("*"," "*(wid-2)))
    # Prints the bottom stars
    print("*"*wid)

# returns a string containing a box with given width and height    
def get_rectangle(width, height):
    # Passes paramenters to local variables
    widt = int(width)
    heig = int(height)
    
    # Creates the format string for the top and bottom stars
    textc = "{0}".format("*"*widt)
    texte = ""
    for k in range(1,heig-1):
        textd = "{0}{1}{0}\n".format("*"," "*(widt-2))
        # Creates the middle string 
        texte += textd
    # Creates the output string
    textf = "{top}\n{middle}{top}".format(top=textc,middle=texte)
    
    return textf
    

# Sample I/O:

# Choose test:
# a
# *****
# *   *
# *   *
# *   *
# *****
# Sample I/O:

# Choose test:
# b 3 4
# calling function
# ***
# * *
# * *
# ***
# called function
# Sample I/O:

# Choose test:
# c 4 3
# calling function
# called function
# ****
# *  *
# ****
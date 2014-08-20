#Author: NLXALE001
#Date: 31 March 2014
#Assignment 4

def print_square():
    print ("*****")
    print ("*   *")
    print ("*   *")
    print ("*   *")
    print ("*****")
    
def print_rectangle(width,height):
    w=width
    h=height
    space=w-2
    print ("*"*w)
    for i in range (1,h-1):
        print ("*", (" "*space), "*",sep="")
    print ("*"*w)
    
def get_rectangle(width,height):
    w=width
    h=height
    space=w-2
    #figure=""
    figure1=["*"*w, "\n"]
    #figure += str(newline)
    for i in range (1,h-1):
        figure1.append("*")
        figure1.append(" "*space)
        figure1.append("*\n")
        #figure += str(newline)
    figure1.append("*"*w)
    figure1.append("\n")
    figure = ""
    for j in range (0, len(figure1)):
        figure = figure + figure1[j]
    figure = str(figure)
    return (figure)
    
    
    
    

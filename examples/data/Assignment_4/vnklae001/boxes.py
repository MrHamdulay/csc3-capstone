#Jeninifer Yuan (YNXYIS001)
#2 April 2014
#Assignment 4, boxes

def print_square(): #prints sqaure with "*" border and spaces within. 
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

def print_rectangle(width,height): #prints get_rectangle(a,b)
    print(get_rectangle(width,height))
       

def get_rectangle(width,height): #prints a rectangle with "*" border and spaces within. 
    x=height
    output=""
    for i in range(1,height+1): #getting top and bottom border - rows of "*"
        if i==1: 
            output+=("*"* width + "\n")
        elif i == height: #getting rows between top and bottom border that end and being with a "*" and have spaces within
            output+=("*"* width)    
        else:
            output+=("*" +(" "*(width-2))+"*" + "\n")
    return output

#Marilynn Bianca Naidoo (NDXMAR020)
#Assignment 4, question 1

def print_square(): #Prints sqaure with "*" border and spaces within. 
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

def print_rectangle(width,height): #Prints get_rectangle(a,b)
    print(get_rectangle(width,height))
       

def get_rectangle(width,height): #Prints a rectangle with "*" border and spaces within. 
    x=height
    out=""
    for i in range(1,height+1): #Getting top and bottom border - rows of "*"
        if i==1: 
            out+=("*"* width + "\n")
        elif i == height: #Getting rows between top and bottom border that end and being with a "*" and have spaces within
            out+=("*"* width)    
        else:
            out+=("*" +(" "*(width-2))+"*"+"\n")
    return out

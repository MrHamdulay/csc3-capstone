#Tejasvin Bagirathi
#Assignment 4, Question 1

def print_square():
    print("*"*5)
    for i in range (0, 3):
        print("*", " "*3, "*", sep="")    
    print("*"*5)

def print_rectangle(w, h):
    print("*"*w)
    for i in range(0, h-2):
        print("*", " "*(w-2), "*", sep="")
    print("*"*w)  

def get_rectangle(w, h):
    x="*"*w + "\n"
    y=""
    for i in range(0, h-2):
        y+=("*" + " "*(w-2) + "*" + "\n")
    z=x
    
    return(x+y+z)


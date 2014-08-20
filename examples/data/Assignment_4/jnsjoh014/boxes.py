#JNSJOH014
#Assignment 4 Question 1

def print_square():
    print("*"*5,sep="")
    for i in range(3):
        print("*","*",sep="   ")
    print("*"*5,sep="")   

def print_rectangle(width,height):
    print("*"*width,sep="")
    for i in range(height-2):
        print("*","*",sep=" "*(width-2))
    print("*"*width,sep="")   
    
def get_rectangle(width,height):
    res = ""
    for i in range(height):
        if i==0 or i==height-1:
            res+=("*"*width)
            res+="\n"
        else:
            res+="*"
            res+=(" "*(width-2))
            res+="*"
            res+="\n"        
    return (res)    
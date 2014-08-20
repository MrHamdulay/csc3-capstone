#Assignment 4
#Question 1 boxes
#Shaheen Karodia
#KRDSHA003
#2014-04-01

def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle (width, height):
    print(width*"*")
    for i in range(height-2):
        print(("*"), (width-2)*(" "), ("*"), sep="")
   
    print(width*"*")
    
def get_rectangle(width, height):
    x=""
    
    
    x=x+(width*"*")
    x=x+"\n"
    for i in range(height-2):
            x=x+"*"+ (width-2)*(" ")+ ("*")
            x=x+("\n")
      
    x=x+(width*"*")    
    return x

    
    
    
    

    
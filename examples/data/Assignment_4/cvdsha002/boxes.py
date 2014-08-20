#Shahrain Coovadia
#CVDSHA002

def print_square():
    print("*"*5)
    a=3
    for i in range(0,a):
        print ("*"+"   "+"*")
    print('*'*5)
    
    
    
def print_rectangle(width,height): 
    print("*"*width)
    for i in range(height-2):
        print("*"+" "*(width-2)+ "*")
    print("*"*width)    
    
    
def get_rectangle(width,height):
    p="*"*width + "\n"
    d=("*" + " "*(width-2) + "*" + "\n")
    return(p + d*(height-2) + p)
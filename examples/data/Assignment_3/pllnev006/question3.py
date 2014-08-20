# Program to print out a message with a frame
# Nevarr Pillay - PLLNEV006
# 20 March 2014

def mess(message,repeat,thick):
    width = len(message) + 2 +2*thick
    torb(width,0,thick,1)
    rep(message,repeat,thick)
    torb(width,thick-1,-1,-1)
    
def rep(message,repeat,thick):
    for i in range(repeat):
        side(thick)
        print(" " + message + " ", end="")
        side(thick)
        print()
        
def side(thick):
    for i in range(thick):
        print("|",end="")
        

def torb(width,start,end,inc):    
    for i in range(start,end,inc):
        side(i)
        print("+",end="")    
        for j in range(width-2*(1+i)):
            print("-",end="")
        print("+",end="")
        side(i)        
        print()
        
def main():
    message = input("Enter the message:\n")
    repeat = eval(input("Enter the message repeat count:\n"))
    thick = eval(input("Enter the frame thickness:\n"))
    mess(message,repeat,thick)
    
main()  


message=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
t=eval(input("Enter the frame thickness:\n"))

def frame(count,t):
    x=len(message)    
    for i in range(t):
        print("|"*(i),"+","-"*(x+(2*t)),"+","|"*(i),sep="")
        x-=2
    
    for i in range(count):
        print("|"*t," ",message," ","|"*t,sep="")
    
    x=len(message)    
    for i in range(t-1,-1,-1):
        print("|"*(i),"+","-"*(x+2),"+","|"*(i),sep="")
        x+=2

frame(count,t)

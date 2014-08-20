#sarayn subroyen
#25 march 2014

def frame():
    a = input("Enter the message:\n")
    b = eval(input("Enter the message repeat count:\n"))
    c = eval(input("Enter the frame thickness:\n"))
    
    i=0
    while i in range(0,c):
        print("|"*(i),"+","-"*(len(a)+2*(c-i)),"+","|"*(i),sep="")
        i+=1
    j=0
    while j in range(0,b):
        print("|"*c,a,"|"*c)
        j+=1
    k=c-1
    while k in range(0,c):
        print("|"*(k),"+","-"*(len(a)+2*(c-k)),"+","|"*(k),sep="")
        k-=1
    
frame()
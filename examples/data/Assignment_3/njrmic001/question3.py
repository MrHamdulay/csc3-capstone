#question3.py
#A program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines
#Author: Michelle Njoroge

def frame():
    x=input("Enter the message:\n")
    y=eval(input("Enter the message repeat count:\n"))
    z=eval(input("Enter the frame thickness:\n"))
    a=len(x)
    line=0
    for i in range(z):
            print("|"*line+"+"+"-"*(a+2*z)+"+"+"|"*line)
            line=line+1
            a=a-2    
    for t in range(y):        
        print("|"*z,x,"|"*z)
    a=len(x)
    l2=z
    for i in range(z):
        if i<=z:
            print("|"*(l2-1)+"+"+"-"*(a+2)+"+"+"|"*(l2-1))
            l2=l2-1
            a+=2        
frame() 




           
    
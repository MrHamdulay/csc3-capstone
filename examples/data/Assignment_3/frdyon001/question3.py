# Name: Yonela Ford
# Student Number: FRDYON001
# Programme to make a frame
# Date: 23 March 2014

def frame():
    x=input("Enter the message:\n")
    y=eval(input("Enter the message repeat count:\n"))
    z=eval(input("Enter the frame thickness:\n"))
    # TOP OF FRAME
    b=z
    for i in range (z):
        print("|"*i, end="")
        print("+","-"*(len(x)+(2*b)),"+",end="",sep="")
        print("|"*i)
        b=b-1
    # MIDDLE OF FRAME:
    for j in range (y):
        print("|"*z,x,"|"*z)
        
    # BOTTOM OF FRAME:
    a=0
    for l in range (z):
        print("|"*(z-l-1),end="")
        print("+","-"*(len(x)+2+2*a),"+",end="",sep="")
        print("|"*(z-l-1))
        a=a+1
        
frame()
#  a program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines
# Budeli Rendani
# BDLREN001
# 26 March 2014

def rendani():
    message=input("Enter the message:\n")
    count=eval(input("Enter the message repeat count:\n"))
    frame=eval(input("Enter the frame thickness:\n"))
    
    a = len(message)
    b=a+frame*2
    c=0
    
    for i in range(frame):
        print("|"*c+"+"+"-"*b+"+"+"|"*c)
        c+=1
        b-=2
    
    for i in range(count):
        print("|"*frame,message,"|"*frame)
        
    b+=2
    c-=1
    
    for i in range(frame):
        print("|"*c+"+"+"-"*b+"+"+"|"*c)
        b+=2
        c-=1
        
rendani()
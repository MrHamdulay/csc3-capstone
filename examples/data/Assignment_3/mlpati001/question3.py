#ATISANG MOLAPO
#STUDENT NUMBER:MLPATI001
#A program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines.
a=input("Enter the message:\n")
b=eval(input("Enter the message repeat count:\n"))
e=eval(input("Enter the frame thickness:\n"))


o = len(a)
z=o+e*2
w=0
for i in range(e):
    print("|"*w+"+"+"-"*z+"+"+"|"*w)
    w+=1
    z-=2
    
for i in range(b):
    print("|"*e,a,"|"*e)
    
z+=2
w-=1

for i in range(e):
    print("|"*w+"+"+"-"*z+"+"+"|"*w)
    z+=2
    w-=1
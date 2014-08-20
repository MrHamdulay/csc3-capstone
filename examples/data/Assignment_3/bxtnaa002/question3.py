# question3.py
# program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines
# author: bxtnaa002

msg = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

n=0
y=1

new = ("|"*thickness)+" "+msg+" "+("|"*thickness) 
length = len(new)

for i in range(0,thickness):
    print("|"*n,"+","-"*(length-(2*y)),"+","|"*n,sep="")
    n = n+1
    y = y+1

for k in range(0,repeat):
    print(new)
    
n = thickness-1

for l in range(0,thickness):
    print("|"*n,"+","-"*(length-(2*y)+2),"+","|"*n,sep="")
    n = n-1
    y = y-1
__author__ = 'George'
message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
length = len(message)
up = 0
for a in range(frame,0,-1):
    print("|"*up,"+","-"*(length+a*2),"+","|"*up,sep="")
    up += 1
for a in range(1,repeat+1):
    print("|"*frame,message,"|"*frame)
up -= 1
for a in range(1,frame+1):
    print("|"*up,"+","-"*(length+a*2),"+","|"*up,sep="")
    up -= 1
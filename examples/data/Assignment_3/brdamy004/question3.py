# Assignment 3 question 3
# Amy Brodie
# 27/03/2014

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
final = " " + message + " "
length = len(final) + (frame*2) -2
inner = 0

for i in range(frame):
    print("|"*inner,"+","-"*length,"+","|"*inner,sep="")
    inner += 1
    length -= 2
for i in range(repeat):
    print("|"*frame,final,"|"*frame,sep="")
for i in range(frame+1,1,-1):
    inner -= 1
    length += 2
    print("|"*inner,"+","-"*length,"+","|"*inner,sep="")
    
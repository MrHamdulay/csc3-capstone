# A program to print an input message repeatedly and contain it within a box
# Author: Jeremy Smith
# Student Number: SMTJER002

message=(input("Enter the message:\n"))
length=len(message)
count=0
repeat=eval(input("Enter the message repeat count:\n"))
framethick=eval(input("Enter the frame thickness:\n"))

for i in range(framethick):
    print("|"*count,"+","-"*(length+2*framethick),"+","|"*count, sep="")
    if i == framethick - 1: 
        continue
    count+=1
    length-=2
for i in range(repeat):
    print("|"*framethick, message, "|"*framethick)
for i in range(framethick):
    print("|"*count,"+","-"*(length+2*framethick),"+","|"*count, sep="")
    count-=1
    length+=2                
#program to a framed message on consecutive lines
#26 March 2014
#Author: Litha Maqungo

message=input("Enter the message:\n")
count=eval(input("Enter the message repeat count:\n"))
box=eval(input("Enter the frame thickness:\n"))
length=len(message)

for i in range(0,box):
    print("|"*i,"+","-"*(length+2*(box-i)),"+","|"*i,sep="")       
for i in range(count):
    print("|"*box,message,"|"*box,end="\n")
for i in range(box-1,-1,-1):
        print("|"*i,"+","-"*(length+2*(box-i)),"+","|"*i,sep="")


        

 
    
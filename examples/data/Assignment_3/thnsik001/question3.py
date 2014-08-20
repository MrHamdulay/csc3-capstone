#Assignment 3
#22/03/2014
#q3
#thnsik001

message=input("Enter the message:\n")
repcount=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
length = len(message)

for i in range(0,thickness):
    print("|"*i,"+",(2*(thickness-i)+length)*"-","+","|"*i,sep="")
    
for j in range(0,repcount):
    print("|"*thickness,message,"|"*thickness)
l=2
for i in range(thickness,0,-1):
    print("|"*(i-1),"+",(length+l)*"-","+","|"*(i-1),sep="")
    l+=2

#Amitha Doodnath
#DDNAMI001
#24/03/2014
#Programme to draw a frame around a message

message=input("Enter the message:\n")

repCount=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
lenMes=len(message)+(thickness*2)

for i in range(thickness):
    print("|"*i,"+","-"*lenMes,"+","|"*i,sep="")
    lenMes-=2

for i in range(repCount):
    print("|"*thickness," ",message," ","|"*thickness,sep="")
    
for i in range(thickness):
    lenMes+=2
    print("|"*(thickness-i-1),"+","-"*lenMes,"+","|"*(thickness-i-1),sep="")
        
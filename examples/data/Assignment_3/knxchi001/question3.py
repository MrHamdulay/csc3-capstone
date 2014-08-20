# Assignment 3
# Question 3

message=input("Enter the message:\n")
repeat= eval(input("Enter the message repeat count:\n"))
frame= eval(input("Enter the frame thickness:\n"))

length= len(message)+(2*frame) 
line= 0
for i in range(frame):
    print("|"*line,"+","-"*length,"+","|"*line,sep="")
    line+=1
    length-=2
    
for i in range(repeat):
    print("|"*frame," ",message," ","|"*frame,sep="")
    
length2= len(message)+2
line= frame-1
for i in range(frame):
    print("|"*line,"+","-"*length2,"+","|"*line,sep="")
    line-=1
    length2+=2
        
     
     
   
    
    
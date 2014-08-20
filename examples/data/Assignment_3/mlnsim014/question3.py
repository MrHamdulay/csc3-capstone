#program to draw frame around a message that has characters
#assignment3, question3
#smanga

message = str(input("Enter the message:\n"))
repetition = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))
k=0

for i in range(thickness,0,-1):
        x = len(message)+2*i
        print("|"*k,"+","-"*x,"+","|"*k,sep="")
        k+=1
          
for i in range(repetition):
        print("|"*(thickness),message,"|"*(thickness))

k=thickness-1
for i in range(thickness):
        x = len(message)+2*(i+1)
        print("|"*k,"+","-"*x,"+","|"*k,sep="")
        k-=1

Message = input("Enter the message:\n")
Repeat = eval(input("Enter the message repeat count:\n"))
Thickness = eval(input("Enter the frame thickness:\n"))
Length = Message.count("")

for i in range(Thickness,0,-1):
        print("|"*(Thickness-i),"+","-"*(Length-1+(2*i)),"+","|"*(Thickness-i),sep="")
        
for j in range(Repeat):
        print("|"*Thickness,Message,"|"*Thickness,sep=" ")

for k in range(Thickness):
        print("|"*(Thickness-(k+1)),"+","-"*(Length+1+(2*k)),"+","|"*(Thickness-(k+1)),sep="")
                

message= input("Enter the message:""\n")
repeat= eval(input("Enter the message repeat count:""\n"))
thickness= eval(input("Enter the frame thickness:""\n"))

for i in range(0,thickness,1):
        print("|"*i,"+",("-"*(len(message)+2*(thickness-i))),"+","|"*i,sep="")


for j in range(0,repeat):
        print("|"*thickness, message, "|"*thickness)

for i in range (thickness-1,-1,-1):
        print("|"*i,"+",("-"*(len(message)+2*(thickness-i))),"+","|"*i,sep="")

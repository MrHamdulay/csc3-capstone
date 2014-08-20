mess=input("Enter the message:\n")
rep=int(input("Enter the message repeat count:\n"))
fra=int(input("Enter the frame thickness:\n"))
length=len(mess)+fra*2



for i in range(fra):
    print("|"*i,"+","-"*length,"+","|"*i,sep="")
    length-=2
    
for j in range(rep):
    print("|"*fra," ",mess," ","|"*fra,sep="")

for k in range(fra):
    print("|"*(fra-1),"+","-"*(length+2),"+","|"*(fra-1),sep="")
    length+=2
    fra-=1
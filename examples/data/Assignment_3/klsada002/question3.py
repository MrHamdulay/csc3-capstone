mess = input("Enter the message:\n")
messrep = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))
numdash = 0
for i in range(0,thick):
    print("|"*i,"+","-"*((len(mess))+thick*2-2*numdash),"+","|"*i,sep="")
    numdash+=1
    
for i in range(0,messrep):
    print("|"*thick,mess,"|"*thick)
    
for i in range(thick-1,-1,-1):
    print("|"*i,"+","-"*((len(mess)+2)+thick*2-2*numdash),"+","|"*i,sep="")
    numdash-=1
    

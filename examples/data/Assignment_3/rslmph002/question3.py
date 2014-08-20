# Mpho Raselo
# question3

msg=input("Enter the message:\n")
foRmsg=0
repCount=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
minus=(len(msg)+2)
for i in range(1,thick,1):
        minus+=2
for x in range(thick):
        print("|"*foRmsg,"+","-"*minus,"+","|"*foRmsg,sep="")
        foRmsg+=1
        minus-=2                
for y in range(repCount):
        print("|"*foRmsg,msg,"|"*foRmsg)
        
for z in range(thick):
        foRmsg-=1
        minus+=2
        print("|"*foRmsg,"+","-"*minus,"+","|"*foRmsg,sep="")




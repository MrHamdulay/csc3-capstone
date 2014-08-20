msg=input("Enter the messege:\n")
w=0
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter frame thickness:\n"))
minus=(len(msg)+2)
for i in range(1,thick,1):
        minus+=2
for x in range(thick):
        print("|"*w,"+","-"*minus,"+","|"*w,sep="")
        w+=1
        minus-=2                
for y in range(repeat):
        print("|"*w,msg,"|"*w)
        
for z in range(thick):
        w-=1
        minus+=2
        print("|"*w,"+","-"*minus,"+","|"*w,sep="")




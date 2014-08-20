message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))

x=len(message)+thick*2+2

y=repeat+thick    

z=0
for i in range(0,thick):
    if z==0:
        print("+"*1,"-"*(x-(2+2*z)),"+"*1, sep="")
    else:
        print("|"*z,"+"*1,"-"*(x-(2+2*z)),"+"*1,"|"*z, sep="")
    z+=1
    
for i in range(0,repeat):
    print("|"*thick, " "*1, message, " "*1, "|"*thick, sep="")
   

for i in range(0,thick):
    w=x-((thick*2))
    print("|"*(thick-1), "+"*1, "-"*w, "+"*1, "|"*(thick-1), sep="")
    thick=thick-1
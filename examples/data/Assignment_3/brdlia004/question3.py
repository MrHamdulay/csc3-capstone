message = input("Enter the message:\n")

repcount = eval(input("Enter the message repeat count:\n"))

fthick = eval(input("Enter the frame thickness:\n"))

space=0
for i in range(fthick,0,-1):
    print('|'*space,end='')  
    print("+"+"-"*(len(message)+i*2)+"+"+'|'*space)
    space+=1 
           

for j in range(repcount):
    print("|"*fthick,message,"|"*fthick)

space=fthick-1
for t in range(0,fthick,1):
    print('|'*space,end='')  
    print("+"+"-"*(len(message)+t*2+2)+"+"+'|'*space)
    space-=1
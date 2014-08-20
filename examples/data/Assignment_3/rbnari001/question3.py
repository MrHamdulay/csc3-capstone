message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

for i in range (0,thickness):
    print("|"*i,"+","-"*(len(message)+((thickness-i)*2)),"+","|"*i,sep="")
    
for j in range (0,repeat):
    print("|"*thickness," ",message," ","|"*thickness,sep="")
    
for k in range (0,thickness):
    print("|"*(thickness-(k+1)),"+","-"*(len(message)+(k+1)*2),"+","|"*(thickness-(k+1)),sep="")

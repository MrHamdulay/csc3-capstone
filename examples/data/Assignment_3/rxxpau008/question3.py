message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

for i in range(thickness):
    if i==0:
        print("+","-"*(thickness),"-"*len(message),"-"*(thickness),"+",sep='')
    else:
        print("|"*i,"+","-"*(thickness-i),"-"*len(message),"-"*(thickness-i),"+","|"*i,sep='')
        
count = 1
while count <=repeat:
    print("|"*thickness," ",message," ","|"*thickness,sep='')
    count+=1
    
for i in range(thickness-1,-1, -1):
    if i==0:
        print("+","-"*(thickness),"-"*len(message),"-"*(thickness),"+",sep='')
    else:
        print("|"*i,"+","-"*(thickness-i),"-"*len(message),"-"*(thickness-i),"+","|"*i,sep='')
    

message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
gap1=0

for i in range(thickness,0,-1):
    print("|"*gap1,"+","-"*(len(message)+2*i),"+","|"*gap1,sep='')
    gap1=gap1+1

for i in range(repeat):
    print("|"*thickness,message,"|"*thickness)
    
for i in range(thickness):
    gap2=thickness-(i+1)
    print("|"*gap2,"+","-"*(len(message)+2*(i+1)),"+","|"*gap2,sep='')
    
    
    
    
    
    





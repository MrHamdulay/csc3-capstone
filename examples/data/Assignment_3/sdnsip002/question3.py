message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))

x=0
y=0
z=1

mes=('|'*thickness)+' '+message+' '+('|'*thickness)
length=len(mes)

for i in range(0,thickness):
    print('|'*y,'+','-'*(length-(2*z)),'+','|'*y,sep='')
    y+=1
    z+=1
    
for k in range(0,repeat):
    print(mes)

y-=1
z-=1

for m in range(thickness,0,-1):
    print('|'*y,'+','-'*(length-(2*z)),'+','|'*y,sep='')
    y-=1
    z-=1
    
   
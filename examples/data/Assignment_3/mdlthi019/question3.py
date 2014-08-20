message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))
line="|"
plus="+"
minus="-"

for a in range(0,thickness,1):
    print(line*a+plus,(minus*(len(message)+2*(thickness-a))),plus+line*a,sep='')
          
for b in range(repeat):
    print(line*thickness+' '+message+' '+line*thickness)
    
for c in range(thickness-1,-1,-1):
    print(line*c+plus,(minus*(len(message)+2*(thickness-c))),plus+line*c,sep='')

    
     
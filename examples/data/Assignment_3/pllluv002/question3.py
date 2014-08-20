x=input("Enter the message:\n")
y=eval(input("Enter the message repeat count:\n"))
z=eval(input("Enter the frame thickness:\n"))
o=y
f=z
d=z
a=len(x)+2
c=a
s=(a+f*2)
e=(d*2-c)
if y==0:
    print()
  
else:
    print("+",((a+z*2)-2)*"-","+",sep="") 
    for i in range((z-1)):
        
        print("|"*(i+1),"+",(s-4)*"-","+","|"*(i+1),sep="")
        z=z+1
        s=s-2
    
    for i in range(y):
        print("|"*(f),x,"|"*(f),sep=" ")

for i in range((d-1)):
        print("|"*(f-i-1),"+",(a*"-" ),"+","|"*(f-i-1),sep="")
        e=e+2
        a=a+2
        
    
        
        
if y!=0:     
        
        
        
    print("+",((c+d*2)-2)*"-","+",sep="") 
    
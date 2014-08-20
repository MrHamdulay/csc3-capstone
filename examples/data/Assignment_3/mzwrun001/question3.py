
msg=input("Enter the message:\n")
msgr=eval(input("Enter the message repeat count:\n"))
thck=eval(input("Enter the frame thickness:\n"))
c1=0
c2=((len(msg)+(2*thck)))
z= "+"
y="-"
x= "|"    
for i in range(thck):
       print((x*c1),z,(y*c2),z,(x*c1),sep="")
       c1+=1
       c2-=2

for i in range(msgr):
       print((x*thck),msg,(x*thck))

c3=thck-1
c4=(len(msg)+2)
for i in range(thck):
       print((x*c3),z,(y*c4),z,(x*c3),sep="")
       c3-=1
       c4+=2



        

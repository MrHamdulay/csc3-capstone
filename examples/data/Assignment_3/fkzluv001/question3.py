msg=input("Enter the message:\n")
c=0;
into=0
msgC=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
mins=(len(msg)+2)
for i in range(1,thick,1):
    mins+=2
for a in range(thick):
    print(into*"|","+","-"*mins,"+",into*"|",sep="")
    into+=1
    mins-=2
for b in range(msgC):
    print(thick*"|",msg,"|"*thick)
for c in range(thick):
    into-=1
    mins+=2
    print(into*"|","+","-"*mins,"+",into*"|",sep="")
    



    



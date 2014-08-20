msg=input("Enter the message:\n")
rpt=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))

l=len(msg) + thick

p=-1

thick1=thick

while thick1>0:
    thick1-=1
    p+=1
    print(p*"|"+"+"+(l+thick)*"-"+"+"+p*"|")
    l-=2
for i in range(rpt):
    print("|"*thick+" ",msg," "+"|"*thick,sep=thick*"")
thick2=thick
while thick2>0:
    l+=2
    print(p*"|"+"+"+(l+thick)*"-"+"+"+p*"|")
    p-=1
    thick2-=1
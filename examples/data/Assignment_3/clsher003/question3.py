message=' '+input("Enter the message:\n")+' '
herhaal=eval(input("Enter the message repeat count:\n"))
raam=eval(input("Enter the frame thickness:\n"))
length=len(message)
count=0
lyn=0
dash=(length+(raam-1)*2)
while(count<raam):
    print("{2}{1}{0}{1}{2}".format('-'*dash,'+','|'*lyn))
    count+=1
    dash-=2
    lyn+=1
for i in range(herhaal):
    print("{0}{1}{0}".format("|"*raam,message))
    
while(count>0):
    lyn-=1
    count-=1
    dash+=2
    print("{2}{1}{0}{1}{2}".format('-'*dash,'+','|'*lyn))
    
    
    
    
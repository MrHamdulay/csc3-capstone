message=input("Enter the message:\n")
length=len(message)
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
looplen=((length)+(thick*2)+2)
nice="{0:+^{1}}".format("-"*(looplen-2),looplen)
p=looplen

for i in range(2,thick+2):
    form="{0:|^{1}}".format(("{0:+^{1}}".format("-"*(p-2),p)),looplen)
    print(form)
    p=p-2
    
for i in range(repeat):
    newm="{0: ^{1}}".format(message,length+2)
    #print(newm)
    pen="{0:|^{1}}".format(newm,looplen)
    print(pen)

p=looplen
    
for i in range(2,thick+2):
    beast="{0:|^{1}}".format(("{0:+^{1}}".format("-"*(p-(thick*2)),((p-(thick*2))+2))),looplen)
    print(beast)
    p=p+2
      
    